from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings
from authentication.forms import UserRegisterForm
from django.core.mail import send_mail
from expense.models import ExpList
from datetime import date

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
           
            subject='Account created'
            message=f'Hello!{username}, your account has been created successfully!'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[email,]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form, 'title':'reqister here'})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            
            if request.user==6:#admin login
                date1=date.today()
                temp=ExpList.objects.all()
                for ctr in temp:
                    date2=ctr.date
                    if (date2-date1).days == 2:    
                        subject='Expense is nearing!'
                        message=f'Hello!{ctr.expense_of}, your {ctr.description} expense of Rs.{ctr.amount} is on {ctr.date}'
                        email_from=settings.EMAIL_HOST_USER
                        recipient_list=[ctr.expense_of.email,]
                        send_mail(subject, message, email_from, recipient_list, fail_silently=False)


            return redirect('index')
        else:
            messages.info(request, 'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form':form, 'title':'log in'})

def index(request):
    return render(request, 'index.html')
