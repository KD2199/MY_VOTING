
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
import urllib
import json
from EVM.models import vote_count,Messages,permission,Voting_details,Draft_Box,LoggedInUser
from django.contrib.auth.decorators import login_required
from django.db.models import F
import time
from Account.models import CandidateData


def home(request):

    return redirect('/')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def count(request,leader_pk):
   
    idata=CandidateData.objects.filter(pk=leader_pk)
    uname=request.user
    
    data=vote_count.objects.get_or_create(UserName=uname)
    vote_count.objects.filter(UserName=uname).update(Number_Of_Votes_You_Cast=F('Number_Of_Votes_You_Cast')+1)
    permission.objects.filter(UserName=uname).update(Condition=True)
    for i in idata:
        Voting_details.objects.get_or_create(UserName=uname,LeaderName=i.Name,Political_Party=i.PartyName)
    messages.success(request,"<--- You Cast Your Vote Successfully --->")

    return redirect('/')

@login_required
def msg(request):
   
   if request.method =='POST':

        username=request.POST['uname']
        subject=request.POST['sub']
        message=request.POST['msg']
        obj=Messages.objects.get_or_create(UserName=username,Subject=subject,Query=message)
        obj1=Draft_Box.objects.get_or_create(UserName=username,Subject=subject,Query=message)
        messages.success(request,"<--- We Will Contact You Soon --->")

   return redirect('/')


@login_required
def voting_list(request):
    
    obj = Voting_details.objects.all()
    return render(request, 'voting_list.html', {'obj': obj})

@login_required
def result(request):
    
    obj=CandidateData.objects.all()
    for i in obj:
        obj1 = Voting_details.objects.filter(LeaderName=i.Name).count()
        CandidateData.objects.filter(Name=i.Name).update(Vote=obj1)

    temp=CandidateData.objects.all()
    return render(request, 'result.html', {'temp': temp})

@login_required
def casted(request):
    
    uname=request.user
    obj1 = Voting_details.objects.filter(UserName=uname)

    return render(request, 'casted.html', {'obj1': obj1})