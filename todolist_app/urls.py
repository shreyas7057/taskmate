from django.urls import path
from .views import *

urlpatterns = [
    path('task/',todolist,name="todolist"),
    path('task/delete/<task_id>',delete_task,name="delete_task"),
    path('task/edit/<task_id>',edit_task,name="edit_task"),
    path('task/complete/<task_id>',complete_task,name="complete_task"),
    path('task/pending/<task_id>',pending_task,name="pending_task"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
]