

from django.urls import path,include
from .views import TaskListView, TaskDetailView, TaskDeleteView, CategoryDetailView, CategoryListView

urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('categoty-list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),


]