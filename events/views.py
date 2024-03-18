from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer,UpcomingEventSerializer
from users.models import CustomUser
from rooms.models import Room
from .models import Event,UpcomingEvent
from django.utils import timezone
from rest_framework.response import Response
from datetime import datetime, timedelta


@api_view(['POST'])
def create_event(request):
    creator_api_key = request.data.get('creator_api_key')
    creator_api_secret_key = request.data.get('creator_api_secret_key')
    room_name = request.data.get('room')

    # API anahtarlarına göre kullanıcıyı bul
    try:
        user = CustomUser.objects.get(api_key=creator_api_key, api_secret_key=creator_api_secret_key)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Odayı adına göre bul
    try:
        room = Room.objects.get(room_name=room_name)
    except Room.DoesNotExist:
        return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

    # Kullanıcının oda sahibi olup olmadığını kontrol et
    if room.creator != user:
        print(room.creator)
        print(user)
        return Response({"message": "You are not authorized to create events in this room"}, status=status.HTTP_403_FORBIDDEN)

    # Event oluşturmak için isteğin geri kalanı ve bulunan kullanıcı ve oda bilgileri ile birlikte bir serializer oluştur
    serializer = EventSerializer(data={
        "creator": user.pk,  # Bulunan kullanıcının kimliğini kullan
        "room": room.pk,  # Bulunan oda nesnesinin kimliğini kullan
        "title": request.data.get('title'),
        "description": request.data.get('description'),
        "date": request.data.get('date'),
        "time": request.data.get('time')
    })

    # Serializer doğruysa kaydet
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, event_id):
    api_key = request.data.get('api_key')
    api_secret_key = request.data.get('api_secret_key')

    # API anahtarlarını kontrol et
    if not api_key or not api_secret_key:
        return Response({"message": "API key and secret key are required"}, status=status.HTTP_400_BAD_REQUEST)

    # API anahtarlarına göre kullanıcıyı doğrula
    try:
        user = CustomUser.objects.get(api_key=api_key, api_secret_key=api_secret_key)
    except CustomUser.DoesNotExist:
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    # Etkinliği al
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    # Etkinliğin sahibi odanın sahibi mi kontrol et
    if event.room.creator != user:
        return Response({"message": "You are not authorized to delete this event"}, status=status.HTTP_401_UNAUTHORIZED)

    # Etkinliği sil
    event.delete()
    return Response({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_event(request, event_id):
    api_key = request.data.get('api_key')
    api_secret_key = request.data.get('api_secret_key')

    # API anahtarlarını kontrol et
    if not api_key or not api_secret_key:
        return Response({"message": "API key and secret key are required"}, status=status.HTTP_400_BAD_REQUEST)

    # API anahtarlarına göre kullanıcıyı doğrula
    try:
        user = CustomUser.objects.get(api_key=api_key, api_secret_key=api_secret_key)
    except CustomUser.DoesNotExist:
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    # Etkinliği al
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    # Etkinliğin sahibi odanın sahibi mi kontrol et
    if event.room.creator != user:
        return Response({"message": "You are not authorized to update this event"}, status=status.HTTP_401_UNAUTHORIZED)

    # Etkinliği güncelle
    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpcomingEventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        now = timezone.now()
        end_time = now + timedelta(days=1)  # Bir sonraki günün başlangıcı

        # Gelecekteki etkinlikleri filtrele
        upcoming_events = Event.objects.filter(date__range=[now.date(), end_time.date()], time__gte=now.time())

        return upcoming_events

@api_view(['GET'])
def list_upcoming_events(request):
    # API anahtarlarını al
    api_key = request.data.get('api_key')
    api_secret_key = request.data.get('api_secret_key')

    # API anahtarlarını kontrol et
    if not api_key or not api_secret_key:
        return Response({"message": "API key and secret key are required"}, status=status.HTTP_400_BAD_REQUEST)

    # API anahtarlarına göre kullanıcıyı doğrula
    try:
        user = CustomUser.objects.get(api_key=api_key, api_secret_key=api_secret_key)
    except CustomUser.DoesNotExist:
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    # UpcomingEventListAPIView sınıfının bir örneğini oluştur
    upcoming_event_list_view = UpcomingEventListAPIView()

    # UpcomingEventListAPIView sınıfının get_queryset metodunu kullanarak verileri al
    queryset = upcoming_event_list_view.get_queryset()

    serializer = UpcomingEventSerializer(queryset, many=True)
    return Response(serializer.data)