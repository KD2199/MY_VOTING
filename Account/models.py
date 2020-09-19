
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=False,default='')
    Profile_Image = models.ImageField(upload_to='Profile_Image', default='user.jpg')
   
    def __str__(self):
        return  f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)
        img=Image.open(self.Profile_Image.path)
        
        if img.width>300 or img.height>300 :
            re_size=(300,300)
            img.thumbnail(re_size)
            img.save(self.Profile_Image.path)


class CandidateData(models.Model):
    
    Name= models.CharField(max_length=50)
    CName=models.CharField(max_length=50)
    SName=models.CharField(max_length=50)
    CN=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    PartyName=models.CharField(max_length=50)
    Application_Status=models.BooleanField(default=False)
    Profile_Image = models.ImageField(upload_to='Profile_Image', default='user.jpg')
    Vote=models.IntegerField(default=0)
   
    def __str__(self):
        return  f'{self.Name} Application'
