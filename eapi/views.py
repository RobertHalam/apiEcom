from django.shortcuts import render

from rest_framework import generics
from rest_framework.utils import serializer_helpers

from .models import BookModel, CategoryModel, ProductModel, Cart
from .serializers import CategorySetializer,BookSetializer,ProductSetializer,CartSetializer

from rest_framework import permissions



# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySetializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySetializer



class ListBook(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BookModel.objects.all()
    serializer_class = BookSetializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BookModel.objects.all()
    serializer_class = BookSetializer


class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BookModel.objects.all()
    serializer_class = BookSetializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSetializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSetializer



class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSetializer