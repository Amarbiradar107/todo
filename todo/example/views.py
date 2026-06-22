from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class Example(APIView):
    def get(self,request):
        return redirect('https://amar-protfolio-2026-june-06.s3.ap-south-1.amazonaws.com/amar.html')

