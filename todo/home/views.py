from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class home(APIView):
    def get(self,request):
        return Response({'message':'Welcome to the To-Do List API!'})