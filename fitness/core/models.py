from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default = True)