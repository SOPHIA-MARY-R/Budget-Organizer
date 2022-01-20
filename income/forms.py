from django import forms
from django.contrib.auth.models import User
from income.models import IncList

class IncListForm(forms.ModelForm):
    class Meta:
        model=IncList
        fields=['source', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }