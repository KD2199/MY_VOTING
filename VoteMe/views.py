
from django.shortcuts import render
from EVM.models import vote_count,Messages,permission,Voting_details,LoggedInUser
from django.contrib.auth.models import User, auth
from Account.models import CandidateData

def home(request):
    
    obj=LoggedInUser.objects.all().count()
    obj1=CandidateData.objects.all().count()
    obj2 = User.objects.all().count()-1

    return render(request, 'index.html', {'obj': obj,'obj1': obj1,'obj2': obj2})