from django.shortcuts import render
import json
from expense.models import ExpList
from income.models import IncList

# Create your views here.
def chart(request):
    exp=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    temp=ExpList.objects.filter(expense_of=request.user)
    for ctr in temp:
        exp[ctr.date.month-1]+=ctr.amount
    inc=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    t=IncList.objects.filter(income_of=request.user)
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
    return render(request, "chart/chart.html", {'janInc':jInc, 'janExp':jExp, 'janSav':jSav, 'febInc':fInc, 'febExp':fExp, 'febSav':fSav, 'marInc':mInc,'marExp':mExp, 'marSav':mSav, 'aprInc':aInc, 'aprExp':aExp, 'aprSav':aSav, 'mayInc':myInc, 'mayExp':myExp, 'maySav':mySav, 'junInc':jnInc, 'junExp':jnExp, 'junSav':jnSav, 'julInc':jlInc, 'julExp':jlExp, 'julSav':jlSav, 'augInc':agInc, 'augExp':agExp, 'augSav':agSav, 'sepInc':sInc, 'sepExp':sExp, 'sepSav':sSav, 'octInc':oInc, 'octExp':oExp, 'octSav':oSav, 'novInc':nInc, 'novExp':nExp, 'novSav':nSav, 'decInc':dInc, 'decExp':dExp, 'decSav':dSav})
