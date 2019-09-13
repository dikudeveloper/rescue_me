from rest_framework import serializers

from ..models import RescueMeProfile


class RescueMeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueMeProfile
        fields = ['id', 'first_name', 'last_name', 'emergency_contacts']