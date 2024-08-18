from django.urls import path
from . import views

urlpatterns = [
    path('alltasks', views.all_tasks, name='all_tasks'),
    path('', views.landing_page, name='landing_page'),
    path('createtask/', views.createtask, name='createtask'),
]
