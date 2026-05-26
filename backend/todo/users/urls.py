
from django.urls import path
from . import views

urlpatterns = [
    path('userlist/', views.Userlist.as_view(), name='userlist'),
    # path('userdetail/<int:id>/', views.UserDetail.as_view(), name='userdetails'),
]

