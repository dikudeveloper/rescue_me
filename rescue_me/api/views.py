from ..models import RescueMeProfile
from .serializers import RescueMeProfileSerializer
from rest_framework import generics


class RescueMeProfileList(generics.ListCreateAPIView):
    queryset = RescueMeProfile.objects.all()
    serializer_class = RescueMeProfileSerializer


class RescueMeProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RescueMeProfile.objects.all()
    serializer_class = RescueMeProfileSerializer