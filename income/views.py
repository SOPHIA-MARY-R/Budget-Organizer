from django.shortcuts import render, redirect
from .models import IncList
from income.forms import IncListForm
# Create your views here.

def create(request):
    if request.method=='POST':
        if request.POST.get('source') and request.POST.get('amount') and request.POST.get('date'):
            saverecord=IncList()
            saverecord.source=request.POST.get('source')
            saverecord.amount=request.POST.get('amount')
            saverecord.date=request.POST.get('date')
            saverecord.income_of=request.user
            saverecord.save()
            return render(request, 'income/create.html')
    else:
        return render(request, 'income/create.html')

def select(request):
    Incomelist=IncList.objects.filter(income_of=request.user)
    return render(request, 'income/select.html', {'Incomelist':Incomelist})

def edit(request, id):
    Incomelist = IncList.objects.get(id= id)
    form = IncListForm(instance=Incomelist)
    if request.method == 'POST':
        form = IncListForm(request.POST, instance=Incomelist)
        if form.is_valid():
            form.save()
            return redirect('/income/select')
    return render(request, 'income/edit.html', {'form':form})

def delete(request, id):
    Incomelist = IncList.objects.get(id= id)
    Incomelist.delete()
    return redirect('/income/select')