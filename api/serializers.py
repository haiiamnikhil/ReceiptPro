from rest_framework import fields, serializers
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

        
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