from rest_framework import fields, serializers
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserRegister(serializers.ModelSerializer):
    profile_image = serializers.FileField()
    
    class Meta:
        model = UserModel
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'gender',
        ]
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegister, self).create(validated_data)
        
        
class UserLogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        
class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        

class ListUsers(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
        
class UserProfileView(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'