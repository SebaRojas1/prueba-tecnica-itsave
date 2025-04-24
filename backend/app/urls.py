from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_all_tasks, name='get_all_tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:id>/complete/', views.mark_task_completed, name='mark_task_completed'),
]