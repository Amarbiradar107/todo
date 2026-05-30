
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [

    # path('userlist/', views.Userlist.as_view(), name='userlist'),
    path('api-token-auth/',obtain_auth_token),
    # path('login/',views.UserLogin.as_view(),name='login'),
    # path('userdetail/<int:id>/', views.UserDetail.as_view(), name='userdetails'),
    path('registration/',views.registration.as_view(),name='logout'),

]

