
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
import urllib
import json
from django.contrib.auth.decorators import login_required
from EVM.models import vote_count, Messages, permission, LoggedInUser, Reply, Draft_Box, Voting_details
from Account.models import Profile,CandidateData
from django.core.mail import send_mail
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from twilio.rest import Client
from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .token_generator import generate_token
# reset password start here
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from sendsms.message import SmsMessage
from sendsms import api
import string
import random
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from .form import ProfileUpdate,UserUpdateForm



def login(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success']:
            print("recaptcha validation successfully")
            username = request.POST['username']
            password = request.POST['password']
            # Checking user is already logged in or not!
            if auth.authenticate(username=username, password=password) is not None:
                obj = User.objects.filter(username=username)
                for i in obj:
                    email = i.email
                    skey = i.pk
                if LoggedInUser.objects.filter(user_id=skey).exists():
                    messages.success(
                        request, "<--- You Are Already Logged In --->")
                else:
                    # initializing size of string
                    N = 7
                    VC = ''.join(random.choices(string.ascii_uppercase +
                                                string.digits, k=N))
                    print("The generated random string : " + str(VC))
                    subject = 'National Voting Portal'
                    message = 'SecretCode For Login Attempt :'+VC + \
                        '\n\nThis Code Will Be Used Only Ones.\n\nThanks & Regards,\nNVP TEAM'
                    email_from = settings.EMAIL_HOST_USER

                    recipient_list = [email, ]
                    send_mail(subject, message, email_from,
                              recipient_list, fail_silently=False)
                    print('SecretCode sent!!')
                    messages.success(
                        request, "<--- SecretCode sent to your registerd email --->")

                    return render(request, 'OTP.html', {'VC': VC, 'username': username, 'password': password})

            else:
                messages.success(
                    request, "<--- You Have Entered Invalid Username or Password --->")
                return redirect('/')

    return redirect('/')


def register(request):

    if request.method == 'POST':

        username = request.POST['uname']
        first_name = request.POST['vid']
        password = request.POST['password']
        password2 = request.POST['pw2']
        email = request.POST['email']
        last_name = request.POST['mo']
        

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.success(request, "* username is already registered")

            elif User.objects.filter(first_name=first_name).exists():
                messages.success(request, "* Epic Id is already registered")

            elif User.objects.filter(email=email).exists():
                messages.success(request, "* Email is already registered")

            elif User.objects.filter(last_name=last_name).exists():
                messages.success(request, "* Mobile No is already registered")

            else:

                is_valid = validate_email(email, verify=True)
                print(is_valid)
                if is_valid == True:

                    user = User.objects.create_user(
                        username=username, first_name=first_name, email=email, password=password, last_name=last_name)
                    user.save()

                    subject = 'National Voting Portal'
                    message = 'Your Registration is Successfully Completed!!'+'\n\nYour Username : ' + \
                        username+'\nYour Password : '+password+'\n\nThanks & Regards,\nNVP TEAM'
                    email_from = settings.EMAIL_HOST_USER

                    recipient_list = [email, ]
                    send_mail(subject, message, email_from,
                              recipient_list, fail_silently=False)
                    print('Confirmation email sent!!')
                    Mobile_No = "+91"+str(last_name)
                    # print(Mobile_No)

                    # message = SmsMessage(body='Your Registration is Successfully Completed!!', from_phone='+41791111111', to=[Mobile_No])
                    # message.send()
                    # api.send_sms(body='I can haz txt', from_phone='+41791111111', to=Mobile_No)

                    # Mobile_No="+91"+str(last_name)

                    # client = Client("AC5233d1103255093b5dbe390f6dc75714", "559af7d6f0efda15a1cfba2a92494801")
                    # client.messages.create(to=Mobile_No,
                    #        from_="+13344633910",
                    #        body=message)

                    obj = permission.objects.create(
                        UserName=username, Condition=False)
                    obj1 = vote_count.objects.create(
                        UserName=username, Number_Of_Votes_You_Cast=0)


                    messages.success(
                        request, "<--- Registration Successfully --->\n\n Confirmation email.")

                else:
                    messages.success(
                        request, "<--- You Have Entered InValid Email Address. Please Verify It. --->")

        else:
            messages.success(
                request, "<--- Password & Confirm Password Didn't Matched! --->")

    return redirect('/')


def logout(request):
    auth.logout(request)
    messages.success(request, "<--- Logout Successfully --->")
    return redirect('/')


@login_required
def profile(request):

    uname = request.user
    data = vote_count.objects.filter(UserName=uname)
    obj = Draft_Box.objects.filter(UserName=uname).count()
    obj3 = Reply.objects.filter(UserName=uname).count()
    obj4 = Profile.objects.filter(user=uname)

    return render(request, 'profile.html', {'data': data, 'obj': obj, 'obj3': obj3,'obj4':obj4})



@login_required
def vote(request):

    uname = request.user
    obj = permission.objects.filter(UserName=uname)
    data = CandidateData.objects.all()

    return render(request, 'voting.html', {'obj': obj, 'data': data})


@login_required
def msg(request):

    obj = Messages.objects.all()
    if request.method == 'POST':
        pk = request.POST['pk']
        username = request.POST['UserName']
        Response = request.POST['msg']
        Subject = request.POST['Subject']
        Query = request.POST['Query']
        obj1 = Reply.objects.get_or_create(
            UserName=username, Subject=Subject, Query=Query, Response=Response)
        Messages.objects.filter(pk=pk).delete()
        obj = Messages.objects.all()
        # print(username,Message)
        messages.success(request, "<--- Reply sent Successfully --->")
        return render(request, 'amsg.html', {'obj': obj})

    return render(request, 'amsg.html', {'obj': obj})


@login_required
def Aprofile(request):
    uname = request.user
    obj1 = User.objects.all().count()-1

    return render(request, 'profile.html', {'obj1': obj1})


def VC(request):
    if request.method == 'POST':

        C1 = request.POST.get('c1')
        C2 = request.POST.get('c2')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(C1,C2,username,password)
        if C1 == C2:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "<--- Login Successfully --->")
                return redirect('/')
        else:
            messages.success(
                request, "<--- SecretCode Verification Failed! --->")
            return redirect('/')

    return redirect('/')


@login_required
def Inbox(request):

    obj = Reply.objects.filter(UserName=request.user)

    return render(request, 'Vmsg.html', {'obj': obj})


@login_required
def Enrlmnt(request):

   # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    data = vote_count.objects.filter(UserName=request.user)
    for i in data:
        count = i.Number_Of_Votes_You_Cast
    obj = User.objects.filter(username=request.user)
    for i in obj:
        f1 = i.username
        Name = "Name : "+i.username
        Email = "Email : "+i.email
        Contact = "Contact No. : "+i.last_name
        Epic = "Epic No. : "+i.first_name
        vote = "Votes You Casted : "+str(count)
        msg1 = "Thanks & Regards ,"
        msg2 = "NVP TEAM."

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setTitle(f1+" 's Eletoral Details")
    p.drawString(250, 800, "Eletoral Details")
    p.drawString(50, 750, Name)
    p.drawString(50, 700, Email)
    p.drawString(50, 650, Contact)
    p.drawString(50, 600, Epic)
    p.drawString(50, 550, vote)
    p.drawString(50, 500, msg1)
    p.drawString(50, 480, msg2)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f1+'.pdf')


@login_required
def Vp(request):

    obj = permission.objects.all().update(Condition=False)
    obj1 = Voting_details.objects.all().delete()
    messages.success(
        request, "<--- Permission Granted To All Users! --->")
    return redirect('/')

@login_required
def pupdate(request):

    if request.method == 'POST':

        # u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            messages.success(request, "<--- Profile Update Successfully --->")
            return redirect('/')

    
    else:
        # u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {'p_form': p_form}
                
    
    return render(request, 'updateprofile.html',context)

    
@login_required
def CR(request):

    if request.method == 'POST':

        Name = request.POST['Fname']
        CName = request.POST['city']
        SName = request.POST['state']
        CN = request.POST['cn']
        Email = request.POST['email']
        PartyName = request.POST['pp']

        if Name== request.user:

            if PartyName=='BJP':

                CandidateData.objects.create(Name=Name,CName=CName,SName=SName,CN=CN,Email=Email,PartyName=PartyName,Profile_Image='bjp.jpg')
                messages.success(request, "<--- Applicataion Submit Successfully!--->")

                return redirect('/')

            elif PartyName=='CGR':

                CandidateData.objects.create(Name=Name,CName=CName,SName=SName,CN=CN,Email=Email,PartyName=PartyName,Profile_Image='cgr.jpg')
                messages.success(request, "<--- Applicataion Submit Successfully!--->")

                return redirect('/')

            elif PartyName=='Others':

                CandidateData.objects.create(Name=Name,CName=CName,SName=SName,CN=CN,Email=Email,PartyName=PartyName,Profile_Image='other.jpg')
                messages.success(request, "<--- Applicataion Submit Successfully!--->")

                return redirect('/')

        else:
            messages.error(request, "<--- You Can't Submit Application Of Other Candidates! --->")
            return redirect('/')



@login_required
def applications(request):
    
    obj=CandidateData.objects.all()

    return render(request, 'Applications.html',{'obj':obj})


@login_required
def approved(request):

    if request.method == 'POST':

        Name = request.POST.get('pk')
        obj=CandidateData.objects.filter(pk=Name).update(Application_Status=True)
        messages.success(request, "<--- Applicataion Approved Successfully!--->")

    return redirect('applications')


@login_required
def status(request):

    if request.method == 'POST':

        Name = request.POST['Fname']
        CName = request.POST['city']
        SName = request.POST['state']
        CN = request.POST['cn']
        Email = request.POST['email']
        PartyName = request.POST['pp']
        obj=CandidateData.objects.filter(Name=request.user).update(Name=Name,CName=CName,SName=SName,CN=CN,Email=Email,PartyName=PartyName)
        messages.success(request, "<--- Applicataion Updated Successfully!--->")
        return redirect('status')

    else:

        obj=CandidateData.objects.filter(Name=request.user)

        return render(request, 'Status.html',{'obj':obj})
