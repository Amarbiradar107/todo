from rest_framework import serializers
from django.contrib.auth.models import User as django_User
from .models import User

#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('name', 'email','password','confirm_password')
#         extra_kwargs = {'password': {'write_only': True},
#                         'confirm_password': {'write_only': True}
#                         }




class registrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = django_User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True},
                        'password2': {'write_only': True}
                        }


    def create(self,validated_data):
        return django_User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data


