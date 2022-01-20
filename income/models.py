from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class IncList(models.Model):
    source=models.CharField(max_length=50)
    amount=models.IntegerField()
    date=models.DateField()
    income_of=models.ForeignKey(User, on_delete=models.CASCADE)

