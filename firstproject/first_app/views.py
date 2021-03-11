from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  my_dict = {'insert_me':"I am from views.py",
              "template": "template is working"
              };
  # return the index.html template
  # the map (my_dict) key should be match withe the 
  # dynamic name on html file
  return render(request,'first_app/index.html', context = my_dict)

def secondapp(request):
    return HttpResponse("<h1>welcome to my api</h1>")


def help(request):

    helpdic = {
        "name" : "lalit",
        "situation": "accident"
    }

    return render(request, 'first_app/help.html', context = helpdic)


def indeximage(request):

    helpdic1 = {
        "name" : "lalit",
        "situation": "accident"
    }

    return render(request,'first_app/imageshow.html', context = helpdic1)
