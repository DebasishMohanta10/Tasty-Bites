from rest_framework import serializers
from .models import Category,MenuItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","username"]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "category-details",
                "lookup_field": "slug"
            }
        }

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(view_name="category-details",lookup_field="slug",queryset=Category.objects.all())
    class Meta:
        model = MenuItem
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "view_name": "menuitems-details",
                "lookup_field": "slug"
            }
        }