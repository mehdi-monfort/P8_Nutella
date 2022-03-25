from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.fields.CharField(max_length=50)
    password = models.fields.CharField(max_length=50)
    email = models.fields.CharField(max_length=100)
    first_name = models.fields.CharField(max_length=50)
    last_name = models.fields.CharField(max_length=50)
