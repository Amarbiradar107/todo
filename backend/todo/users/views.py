from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth.models import User as django_User
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import  registrationSerializer


# class Userlist(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         userdetails = User.objects.all()
#         serializer = UserSerializer(userdetails, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request):
#         user_name = request.data.get('user_name')
#         if user_name=="":
#             return Response({'error': 'user_name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
#         user_mail = request.data.get('email')
#         if user_mail=="":
#             return Response({'error': 'email cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
#         if user_mail == User.objects.filter(email=user_mail).first():
#             return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#         # if User.objects.filter(username=user_name).exists():
#         #     return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
#         password = request.data.get('password')
#         confirm_password = request.data.get('confirm_password')
#         if password != confirm_password:
#             return Response({'error': 'passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class registration(APIView):

    def post(self,request):
        serializer = registrationSerializer(data=request.data)
        password_1 = request.data.get('password')
        password_2 = request.data.get('password2')
        data={}
        if password_1 != password_2:
            return Response({'error': 'passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        user_email = request.data.get('email')
        email = django_User.objects.filter(email=user_email).first()
        if email:
            return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            account = serializer.save()
            data['registration'] = 'account created successfully'
            data['user_name'] = account.username
            data['email'] = account.email
            data['token'] = Token.objects.create(user=account).key
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Logout(APIView):

    def post(self,request):
        print(request.user.auth_token)
        request.user.auth_token.delete()
        return Response({'data':"logout successfully"},status=status.HTTP_200_OK)











