from django.urls import path
from django.conf.urls import url
from first_app import views

urlpatterns =[
    
    # don't give "" in the name 
    url('', views.secondapp, name = 'secondapp'),
]