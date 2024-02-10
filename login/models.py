from django.db import models
class Users(models.Model):
  user_email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)