from django.urls import path
from . import views

app_name = 'task_manager'
urlpatterns = [
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/update/', views.update_task, name='update_task'),
    path('task/list/', views.task_list, name='task_list'),
    path('task/<int:task_id>/change-status/', views.change_task_status, name='change_task_status'),
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/update/', views.update_task, name='update_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
