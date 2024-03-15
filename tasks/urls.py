# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Lists all tasks
    path('create/', views.task_create, name='task_create'),  # Form to create a new task
    path('update/<int:pk>/', views.task_update, name='task_update'),  # Form to update a task
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),  # Confirm delete a task
]
