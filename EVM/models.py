from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL



class vote_count(models.Model):
    UserName= models.CharField(max_length=50,blank=False,default="")
    Number_Of_Votes_You_Cast = models.IntegerField(blank=True,default=0)
    


    def __str__(self):
        return '{}'.format(self.UserName)

        

class Messages(models.Model):
    UserName= models.CharField(max_length=50)
    Subject= models.CharField(max_length=50)
    Query= models.TextField(max_length=300)
  

    def __str__(self):
        return self.UserName


class permission(models.Model):
    UserName= models.CharField(max_length=50,blank=False,default="")
    Condition=models.BooleanField(default=False)
    
    def __str__(self):
        return '{}'.format(self.UserName)


class Voting_details(models.Model):
    
    UserName= models.CharField(max_length=50)
    LeaderName= models.CharField(max_length=50)
    Political_Party= models.CharField(max_length=50)
   
    def __str__(self):
        return self.UserName
    

# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user',on_delete=models.CASCADE,null=True)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=False,blank=False)

    def __str__(self):
        return self.user.username

class Reply(models.Model):
    UserName= models.CharField(max_length=50)
    Subject= models.CharField(max_length=50,null=False,default=" ")
    Query= models.TextField(max_length=300,default=" ")
    Response= models.TextField(max_length=300)

    def __str__(self):
        return self.UserName

class Draft_Box(models.Model):
    UserName= models.CharField(max_length=50)
    Subject= models.CharField(max_length=50)
    Query= models.TextField(max_length=300)
  

    def __str__(self):
        return self.UserName


