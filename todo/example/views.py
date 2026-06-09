from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class Example(APIView):
    def get(self,request):
        data = {
            'message': 'This is an example API endpoint.',
            'status': 'success'
        }
        return Response(data)

