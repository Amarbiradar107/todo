from rest_framework import serializers
from .models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_id', 'title','description','priority','status','due_date','created_at','updated_at','is_deleted')
        extra_kwargs ={
            'created_at': {'read_only':True},
            'updated_at': {'read_only':True},
            'is_deleted': {'read_only':True},
        }


    def create(self, **validated_data):
        task = Task(**validated_data)
        task.save()
        return task


    def update(self, instance, **validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.status = validated_data.get('status', instance.status)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.save()
        return instance



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name', 'created_at', 'updated_at', 'is_deleted')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'is_deleted': {'read_only': True},
        }



