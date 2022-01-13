from django import forms
from . models import ExpList, IncList

class ExpListForm(forms.ModelForm):
    class Meta:
        model = ExpList
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'})
        }

class IncListForm(forms.ModelForm):
    class Meta:
        model = IncList
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'})
        }

