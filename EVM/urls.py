'''
  @author Karan Dave  
'''

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='HomePage'),
    path('count/<int:leader_pk>', views.count, name="count"),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('msg/', views.msg, name='msg'),
    path('voting_list/', views.voting_list, name='voting_list'),
    path('result/', views.result, name='result'),
    path('casted/', views.casted, name='casted'),
   
]
