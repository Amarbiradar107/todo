from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from  .permission import IsAdminOrReadOnly


# Create your views here.


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        task_list = Task.objects.filter(is_deleted=False)
        serializer_class = TaskSerializer(task_list, many=True)
        return Response(serializer_class.data)


    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]

    def get(self,request,pk):
        task = get_object_or_404(Task, pk=pk, is_deleted=False)
        if task.is_deleted:
            return Response({'detail': 'Task already deleted.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self,request,pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request,pk):
    #     task = Task.objects.get(pk=pk)
    #     task.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class TaskDeleteView(APIView):
    Permission_classes = [IsAdminOrReadOnly,IsAuthenticated]
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.is_deleted:
            return Response({'detail': 'Task already deleted.'}, status=status.HTTP_400_BAD_REQUEST)
        task.is_deleted = True
        task.save()
        return Response({'detail': 'Task soft-deleted.'}, status=status.HTTP_200_OK)

    # def put(self,request,pk):
    #     task = Task.objects.get(pk=pk)
    #     serializer = TaskSerializer(instance=task, data=request.data)
    #     print(serializer.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]
    def get(self,request):
        category_list = Category.objects.filter(is_deleted=False)
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)


    def post(self,request):
        # Check for duplicate category name
        category_name = request.data.get('category_name')
        if Category.objects.filter(category_name=category_name, is_deleted=False).exists():
            return Response({'detail': 'Category with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]
    def get(self,request,pk):
        category = get_object_or_404(Category, pk=pk,is_deleted=False)
        # if category.is_deleted:
        #     return Response({'detail': 'Category already deleted.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self,request,pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        category = get_object_or_404(Category, pk=pk)
        category.is_deleted = True
        category.save()
        return Response({'detail': 'Category soft-deleted.'}, status=status.HTTP_200_OK)


