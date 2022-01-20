from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExpList(models.Model):
    description=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    amount=models.IntegerField()
    date=models.DateField()
    expense_of=models.ForeignKey(User, on_delete=models.CASCADE)
