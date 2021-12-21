from django.db import models
from rest_framework import serializers
from .models import CategoryModel,BookModel,ProductModel,Cart

class CategorySetializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'title'
        ]
        model = CategoryModel



class BookSetializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BookModel
        


class ProductSetializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProductModel
        

class CartSetializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Cart
        