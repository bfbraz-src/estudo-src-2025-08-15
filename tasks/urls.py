from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskslist, name='task_lists'),
    path('tasks/', views.tasks),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
