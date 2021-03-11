
from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import include

urlpatterns = [
    path('index/',views.index, name ="index"),
    path('indeximage/', views.indeximage, name = "indeximage"),
    path('help/', views.help, name = "help"),
    path('firstapp/',include('first_app.urls') ),
    path('admin/', admin.site.urls)
]
