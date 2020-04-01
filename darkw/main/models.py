from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class users(models.Model):
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)