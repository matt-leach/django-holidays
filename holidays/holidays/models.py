from django.db import models
from django.contrib.auth.models import User


class Holiday(models.Model):
    user = models.ForeignKey(User, related_name="holidays")
    start_date = models.DateField()
    end_date = models.DateField()
    