from django.contrib import admin
from basic_app import views
from django.conf.urls import url


# template tagging
# we need to set app_name to use the url links in the template
app_name = 'basic_app'


urlpatterns = [
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other'),

]