from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='owner.username')  # creator alanıyla ilişkili olan owner alanını belir

    class Meta:
        model = Room
        fields = ['id', 'room_name', 'creator']
