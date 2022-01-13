from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

categoryChoices=(
    ('Housing', 'Housing'),
    ('Travel', 'Travel'),
    ('Transportation', 'Transportation'),
    ('Insurance', 'Insurance'),
    ('Tution', 'Tution'),
    ('Utilities', 'Utilities'),
    ('Food', 'Food'), 
    ('Entertainment', 'Entertainment'),
    ('Health care', 'Health care'),
    ('Other', 'Other'),
)

sourceChoices=(
    ('Job Salary', 'Job Salary'),
    ('Profit Sale', 'Profit Sale'),
    ('Profit Stock', 'Profit Stock'),
    ('Heist', 'Heist'),
    ('Treasure', 'Treasure'),
    ('Scam', 'Scam'),
    ('Other', 'Other'),
)
class ExpList(models.Model):
    expense = models.CharField(max_length=100)
    amount = models.FloatField()
    category=models.CharField(max_length=100, choices=categoryChoices)
    date = models.DateField()
    expense_of = models.ForeignKey(User, on_delete=models.CASCADE)

class IncList(models.Model):
    source = models.CharField(max_length=100, choices=sourceChoices)
    amount = models.FloatField()
    date = models.DateField()
    income_of = models.ForeignKey(User, on_delete=models.CASCADE)




