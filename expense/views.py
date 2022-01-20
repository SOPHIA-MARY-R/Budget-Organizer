from django.shortcuts import render, redirect
from .models import ExpList
from expense.forms import ExpListForm
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def ecreate(request):
    if request.method=='POST':
        if request.POST.get('description') and request.POST.get('category') and request.POST.get('amount') and request.POST.get('date'):
            saverecord=ExpList()
            saverecord.description=request.POST.get('description')
            saverecord.category=request.POST.get('category')
            saverecord.amount=request.POST.get('amount')
            saverecord.date=request.POST.get('date')
            saverecord.expense_of=request.user
            saverecord.save()

            date1=date.today()
            temp=ExpList.objects.filter(expense_of=request.user)
            for ctr in temp:
                date2=ctr.date
                if (date2-date1).days == 2:    
                    subject='Expense is nearing!'
                    message=f'Hello!{request.user}, this is from Budget Organizer team, your {saverecord.description} expense of Rs.{saverecord.amount} is on {saverecord.date}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[request.user.email,]
                    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            return render(request, 'expense/ecreate.html')
    else:
        return render(request, 'expense/ecreate.html')

def eselect(request):
    Expenselist=ExpList.objects.filter(expense_of=request.user)

    temp=ExpList.objects.filter(expense_of=request.user)
    date1=date.today()
    for ctr in temp:
        date2=ctr.date
        if (date2-date1).days == 2:
            subject='Your expense is nearing!!'
            message=f'Hello!{request.user}, this is from Budget Organizer team, your {ctr.description} expense of Rs.{ctr.amount} is on {ctr.date}'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[request.user.email,]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)

    return render(request, 'expense/eselect.html', {'Expenselist':Expenselist})

def eedit(request, id):
    Expenselist = ExpList.objects.get(id= id)
    form = ExpListForm(instance=Expenselist)
    if request.method == 'POST':
        form = ExpListForm(request.POST, instance=Expenselist)
        if form.is_valid():
            form.save()

            date1=date.today()
            temp=ExpList.objects.filter(expense_of=request.user)
            for ctr in temp:
                date2=ctr.date
                if (date2-date1).days == 2:    
                    subject='Expense is nearing!'
                    message=f'Hello!{request.user}, your {ctr.description} expense of Rs.{ctr.amount} is on {ctr.date}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[request.user.email,]
                    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            return redirect('/expense/eselect')
    return render(request, 'expense/eedit.html', {'form':form})

def edelete(request, id):
    Expenselist = ExpList.objects.get(id= id)
    Expenselist.delete()
    return redirect('/expense/eselect')
