from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import mailForm
from .models import mail
# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')