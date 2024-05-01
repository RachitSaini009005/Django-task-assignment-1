# task_automation/urls.py
from django.urls import path
from .views import create_files ,index

urlpatterns = [
    path('create_files/',create_files, name='create_files'),
    path('', index, name='index'),
]
