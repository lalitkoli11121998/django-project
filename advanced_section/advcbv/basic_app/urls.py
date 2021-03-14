from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.ScholDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete')
]
