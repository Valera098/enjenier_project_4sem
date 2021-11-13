from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour = models.ForeignKey('api.Tour', on_delete=models.CASCADE)
    buy_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()