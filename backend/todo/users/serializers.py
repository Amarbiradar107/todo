from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email','password','confirm_password')
        extra_kwargs = {'password': {'write_only': True},
                        'confirm_password': {'write_only': True}
                        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.confirm_password = validated_data.get('confirm_password', instance.confirm_password)
        instance.save()
        return instance




