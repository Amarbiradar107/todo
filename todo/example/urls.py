
from django.urls import path,include
from .views import Example

urlpatterns = [
    path('', Example.as_view(), name='example'),
]