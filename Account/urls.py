'''
  @author Karan Dave  
'''

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('VC/', views.VC, name='VC'),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('vote/', views.vote, name="vote"),
    path('msg/', views.msg, name='msg'),
    path('Aprofile/', views.Aprofile, name="Aprofile"),
    path('Inbox/', views.Inbox, name="Inbox"),
    path('Enrlmnt/', views.Enrlmnt, name="Enrlmnt"),
    path('Vp/', views.Vp, name="Vp"),   
    path('pupdate/', views.pupdate, name="pupdate"),
    path('CR/', views.CR, name="CR"),
    path('applications/', views.applications, name="applications"),
    path('approved/', views.approved, name="approved"),
    path('status/', views.status, name="status"),
    # path('Reset_Password/', views.Reset_Password, name="Reset_Password"),
    # # path('update/', views.update, name="update"),
    # path('findAc/', views.findAc, name="findAc"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url='accounts/password_change/done/'), name="PasswordChangeView"),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView, name="PasswordChangeDoneView"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(success_url='done/'), name="PasswordResetView"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView, name="PasswordResetDoneView"),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url='/accounts/reset/done/'), name="PasswordResetConfirmView"),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView, name="PasswordResetCompleteView"),
    

]
