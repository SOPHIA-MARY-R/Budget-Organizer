from django import forms
from django.contrib.auth.models import User
from expense.models import ExpList

class ExpListForm(forms.ModelForm):
    class Meta:
        model=ExpList
        fields=['description', 'category', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }