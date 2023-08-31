from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import CategorySerializer,MenuItemSerializer,UserSerializer
from .models import Category,MenuItem
from .permissions import ManagerPermissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.models import User,Group
from rest_framework.response import Response
from rest_framework import status

class CategoryListViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method != "GET":
            permission_classes = [ManagerPermissions]
        return [permission() for permission in permission_classes]
        

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_classes = [ManagerPermissions]
        return [permission() for permission in permission_classes]
    
class MenuItemListView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields= ["price","featured"]
    search_fields = ["title","category__title"]
    filterset_fields=["category"]
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_classes = [ManagerPermissions]
        return [permission() for permission in permission_classes]
    
class MenuItemsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = "slug"
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_classes = [ManagerPermissions]
        return [permission() for permission in permission_classes]

class AddManger(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    
    def list(self,request):
        group = Group.objects.get(name="Manager")
        managers = group.user_set.all()
        serialized_items = UserSerializer(managers,many=True)
        return Response(serialized_items.data,status.HTTP_200_OK)
    
    def create(self,request):
        username = request.data["username"]
        
        if username:
            group = Group.objects.get(name="Manager")
            user = get_object_or_404(User,username=username)
            group.user_set.add(user)
            return Response({"message": f"User {username} added to Manager's group successfully!"},status.HTTP_200_OK)
        return Response({"message": "Something went Wrong!"},status.HTTP_404_NOT_FOUND)

class RemoveManager(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    
    def destroy(self,request,username):
        groups = Group.objects.get(name="Manager")
        user = get_object_or_404(User,username=username)
        groups.user_set.remove(user)
        return Response({"message": "User removed from Manager's group successfully!!"},status.HTTP_200_OK)