from django.shortcuts import render, redirect
from .forms import ExpListForm
from .forms import IncListForm
from .models import ExpList
from .models import IncList
import json
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

def select(req):
    Expenselist = ExpList.objects.filter(expense_of=req.user).order_by('date')
    temp=ExpList.objects.filter(expense_of=req.user)
    date1=date.today()
    for ctr in temp:
        date2=ctr.date
        if (date2-date1).days == 2:
            subject='Your expense is nearing!!'
            message=f'Hello!{req.user}, this is from Budget Organizer team, your {ctr.expense} expense of Rs.{ctr.amount} is nearing in 2 days.'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=['recipient mail ID',]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    #return HttpResponse("Mail sent to you!!")
    return render(req, 'select.html', {'Expenselist':Expenselist})

def selectIncome(req):
    Incomelist = IncList.objects.filter(income_of=req.user).order_by('date')
    return render(req, 'selectincome.html', {'Incomelist':Incomelist})

def Insert(req):
    if req.method == 'POST':
        form = ExpListForm(req.POST)
        if form.is_valid():
            form.save()
            temp=ExpList.objects.filter(expense_of=req.user)
            date1=date.today()
            for ctr in temp:
                date2=ctr.date
                if (date2-date1).days == 2:
                    subject='Your expense is nearing!!'
                    message=f'Hello!{req.user}, this is from Budget Organiizer team, your {ctr.expense} expense of Rs.{ctr.amount} is nearing in 2 days.'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=['recipient mail ID',]
                    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            return redirect('/elist/select')
        else:
            form = ExpListForm()
    form = ExpListForm()
    temp=ExpList.objects.filter(expense_of=req.user)
    date1=date.today()
    for ctr in temp:
        date2=ctr.date
        if (date2-date1).days == 2:
            subject='Your expense is nearing!!'
            message=f'Hello!{req.user}, your {ctr.expense} expense of Rs.{ctr.amount} is nearing in 2 days.'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=['recipient mail ID',]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return render(req, 'create.html', {'form':form})
    
def InsertIncome(req):
    if req.method == 'POST':
        form = IncListForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/elist/selectincome')
        else:
            form = IncListForm()
    form = IncListForm()
    return render(req, 'createincome.html', {'form':form})

def edit(req, id):
    Expenselist = ExpList.objects.get(id= id)
    form = ExpListForm(instance=Expenselist)
    if req.method == 'POST':
        form = ExpListForm(req.POST, instance=Expenselist)
        if form.is_valid():
            form.save()
            temp=ExpList.objects.filter(expense_of=req.user)
            date1=date.today()
            for ctr in temp:
                date2=ctr.date
                if (date2-date1).days == 2:
                    subject='Your expense is nearing!!'
                    message=f'Hello!{req.user}, your {ctr.expense} expense of Rs.{ctr.amount} is nearing in 2 days.'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=['recipient mail ID',]
                    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            return redirect('/elist/select')
    return render(req, 'edit.html', {'form':form})

def editIncome(req, id):
    Incomelist = IncList.objects.get(id= id)
    form = IncListForm(instance=Incomelist)
    if req.method == 'POST':
        form = IncListForm(req.POST, instance=Incomelist)
        if form.is_valid():
            form.save()
            return redirect('/elist/selectincome')
    return render(req, 'editincome.html', {'form':form})

def delete(req, id):
    Expenselist = ExpList.objects.get(id= id)
    Expenselist.delete()
    return redirect('/elist/select')

def deleteIncome(req, id):
    Incomelist = IncList.objects.get(id= id)
    Incomelist.delete()
    return redirect('/elist/selectincome')

def chart(req):
    exp=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    temp=ExpList.objects.filter(expense_of=req.user)
    for ctr in temp:
        exp[ctr.date.month-1]+=ctr.amount
    inc=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    t=IncList.objects.filter(income_of=req.user)
    for ctr in t:
        inc[ctr.date.month-1]+=ctr.amount
    janExp, janInc, janSav = exp[0], inc[0], inc[0]-exp[0]
    febExp, febInc, febSav = exp[1], inc[1], inc[1]-exp[1]
    marExp, marInc, marSav = exp[2], inc[2], inc[2]-exp[2]
    aprExp, aprInc, aprSav = exp[3], inc[3], inc[3]-exp[3]
    mayExp, mayInc, maySav = exp[4], inc[4], inc[4]-exp[4]
    junExp, junInc, junSav = exp[5], inc[5], inc[5]-exp[5]
    julExp, julInc, julSav = exp[6], inc[6], inc[6]-exp[6]
    augExp, augInc, augSav = exp[7], inc[7], inc[7]-exp[7]
    sepExp, sepInc, sepSav = exp[8], inc[8], inc[8]-exp[8]
    octExp, octInc, octSav = exp[9], inc[9], inc[9]-exp[9]
    novExp, novInc, novSav = exp[10], inc[10], inc[10]-exp[10]
    decExp, decInc, decSav = exp[11], inc[11], inc[11]-exp[11]
    jInc, jExp, jSav = json.dumps(janInc), json.dumps(janExp), json.dumps(janSav)
    fInc, fExp, fSav = json.dumps(febInc), json.dumps(febExp), json.dumps(febSav)
    mInc, mExp, mSav = json.dumps(marInc), json.dumps(marExp), json.dumps(marSav)
    aInc, aExp, aSav = json.dumps(aprInc), json.dumps(aprExp), json.dumps(aprSav)
    myInc, myExp, mySav = json.dumps(mayInc), json.dumps(mayExp), json.dumps(maySav)
    jnInc, jnExp, jnSav = json.dumps(junInc), json.dumps(junExp), json.dumps(junSav)
    jlInc, jlExp, jlSav = json.dumps(julInc), json.dumps(julExp), json.dumps(julSav)
    agInc, agExp, agSav = json.dumps(augInc), json.dumps(augExp), json.dumps(augSav)
    sInc, sExp, sSav = json.dumps(sepInc), json.dumps(sepExp), json.dumps(sepSav)
    oInc, oExp, oSav = json.dumps(octInc), json.dumps(octExp), json.dumps(octSav)
    nInc, nExp, nSav = json.dumps(novInc), json.dumps(novExp), json.dumps(novSav)
    dInc, dExp, dSav = json.dumps(decInc), json.dumps(decExp), json.dumps(decSav)
    return render(req, "chart.html", {'janInc':jInc, 'janExp':jExp, 'janSav':jSav, 'febInc':fInc, 'febExp':fExp, 'febSav':fSav, 'marInc':mInc,'marExp':mExp, 'marSav':mSav, 'aprInc':aInc, 'aprExp':aExp, 'aprSav':aSav, 'mayInc':myInc, 'mayExp':myExp, 'maySav':mySav, 'junInc':jnInc, 'junExp':jnExp, 'junSav':jnSav, 'julInc':jlInc, 'julExp':jlExp, 'julSav':jlSav, 'augInc':agInc, 'augExp':agExp, 'augSav':agSav, 'sepInc':sInc, 'sepExp':sExp, 'sepSav':sSav, 'octInc':oInc, 'octExp':oExp, 'octSav':oSav, 'novInc':nInc, 'novExp':nExp, 'novSav':nSav, 'decInc':dInc, 'decExp':dExp, 'decSav':dSav})











    