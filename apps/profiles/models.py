from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.OneToOneField(User, related_name='rating')
    points = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Bonus(models.Model):
    points = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255)
