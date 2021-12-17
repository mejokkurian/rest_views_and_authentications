from django.db.models import fields
from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

from checking import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'dicription',]
     
        
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id', 'username', 'password']
        
        extra_kwargs = {'password':{
        'write_only':True,
        'required' : True
        }}
        
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user
        
