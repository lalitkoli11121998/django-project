from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
# . means current directory
from . import models
# Create your views here.

# def index(request):
#     return render(request, 'index.html')


# here we does not call the function as function view
# we call the class view

class CBView(View):

    # here get method is not a simple method it is a get request
    # whenever get request is come through the class this method will
    # call
    def get(self,request):
        return HttpResponse("class bases views are cool")


# class IndexView(TemplateView):

#     template_name = 'index.html'
#     # ** --> key word argument (name ="one", age = 27, clg ="ymca")
#     # * only argument as touple (1,2,3)
#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)

#         context['injectme'] = "basic function"
#         return context


# list of school
class SchoolListView(ListView):
    context_object_name = 'school_list'
    # get list of school using model, list view given the list and put in the 
    # school_list object
    model = models.School
    template_name = 'basic_app/school_list.html'
    # if we call this class then it will given the list of models.School type of object
    # we can print or access the list by school_list where school is the model name but all
    # letter should be lower case

# detail of each school
class ScholDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'



class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School

    # it means when you seccessful delete the school item you redirect to the 
    #  basic_app/list templates
    # lazy used because we want when whole proces done then we redirect
    success_url = reverse_lazy("basic_app:list")