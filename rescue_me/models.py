from django.db import models
from django.contrib.auth.models import User


class RescueMeProfile(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    emergency_contacts = models.TextField()

    class Meta:
        ordering = ['create_date']
