from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email','password','confirm_password')
        extra_kwargs = {'password': {'write_only': True},
                        'confirm_password': {'write_only': True}
                        }

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        if email=="":
            raise serializers.ValidationError('Email cannot be empty')
        return email

    def validate_username(self, username):
        if username=="":
            raise serializers.ValidationError('Username cannot be empty')
        return username

    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError('Password cannot be empty')
        return password

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data

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




