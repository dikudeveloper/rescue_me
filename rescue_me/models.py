from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
