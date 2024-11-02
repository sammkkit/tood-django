from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/create/', views.create_todo, name='create_todo'), 
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
]
