
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .serializers import UserSerialzer
from .models import Post
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from checking import serializers
# Create your views here.

# --------------------------------  normal view ---------------------------------------- # 
@api_view(['GET', 'POST' , 'PUT', 'DELETE'])
def post(request):
    if request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializer(post,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    

 # --------------------------------  normal view ---------------------------------------- # 
# @api_view(['POST' , 'PUT', 'DELETE'])
# def details(request, pk):
#     post = Post.objects.get(pk = pk)
#     if request.method == 'PUT':
#         serializer = PostSerializer(post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_200_OK)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)  


    # ----------------------- mixins viewset ------------------------------------------------- #
class details(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request):
        return self.list(request)
            
            
    def post(self, request):
        return self.create(request)
    
    
   #-------------------------------------- view using mixins---------------------------------------------------------------- #
# class class_details(generics.GenericAPIView,mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
#     lookup_field = 'id'
    
    
#     def get(self, request,id):
#         return self.retrieve(request,id =id)
    
#     def put(self, request,id):
#         return self.update(request,id = id)
    
    
#     def delete(self, request,id):
#         return self.destroy(request,id = id)
    
    
    
 # ------------------------------ generic viewset using mixins ------------------------------------------ #
  
# class class_details(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
    
   # --------------------------- model viewset ------------------------------- # 
class class_details(viewsets.ModelViewSet):  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # tokem authentication
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    

# ___________________ user creations ________________ #  
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
    
    
    
        
    
                    
                    
    
        
    