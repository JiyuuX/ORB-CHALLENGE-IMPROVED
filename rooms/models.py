from django.db import models
from users.models import CustomUser

class Room(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_rooms', null=True, blank=True)
    subscribers = models.ManyToManyField(CustomUser, related_name='subscribed_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
