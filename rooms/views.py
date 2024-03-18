from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Room
from .serializers import RoomSerializer
from users.models import CustomUser
from events.serializers import EventSerializer
from events.models import Event

@api_view(['POST'])
def create_room(request):
    api_key = request.data.get('api_key')
    api_secret_key = request.data.get('api_secret_key')

    if not api_key or not api_secret_key:
        return Response({"message": "API key and secret key are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(api_key=api_key, api_secret_key=api_secret_key)
    except CustomUser.DoesNotExist:
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        # Oda yaratıcısını belirlemek için creator alanını set et
        serializer.validated_data['creator'] = user
        serializer.save()
        return Response({"message": "Room created successfully", "room": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def subscribe_room(request):
    api_key = request.data.get('api_key')
    api_secret_key = request.data.get('api_secret_key')
    room_name = request.data.get('subscribe')

    if not api_key or not api_secret_key:
        return Response({"message": "API key and secret key are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(api_key=api_key, api_secret_key=api_secret_key)
    except CustomUser.DoesNotExist:
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        room = Room.objects.get(room_name=room_name)
    except Room.DoesNotExist:
        return Response({"message": "Room does not exist"}, status=status.HTTP_404_NOT_FOUND)

    user.subscribed_rooms.add(room)
    return Response({"message": "Subscribed to room successfully"}, status=status.HTTP_200_OK)


class RoomEventsAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']

        # Istegi yapan kullanicinin kimligini dogrula
        api_key = self.request.data.get('api_key')
        api_secret_key = self.request.data.get('api_secret_key')

        if not api_key or not api_secret_key:
            return Response({"message": "API key and secret key are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(api_key=api_key, api_secret_key=api_secret_key)
        except CustomUser.DoesNotExist:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        # Kullaniciyi odaya abone yapmış mı kontrol et
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({"message": "Room does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if user.subscribed_rooms.filter(id=room_id).exists():
            # Kullanici odaya abone ise, oda olaylarini listele
            return Event.objects.filter(room__id=room_id)
        else:
            return Response({"message": "Unauthorized. User is not subscribed to this room"},
                            status=status.HTTP_401_UNAUTHORIZED)