from django.urls import path
from .views import create_room
from .views import subscribe_room
from .views import RoomEventsAPIView

urlpatterns = [
    path('create/', create_room, name='create-room'),
    path('subscribe/', subscribe_room, name='subscribe-room'),
    path('<int:room_id>/events/', RoomEventsAPIView.as_view(), name='room-events'),
]
