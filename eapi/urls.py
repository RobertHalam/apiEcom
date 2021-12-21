from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import DetailCart, ListBook, ListCart,ListCategory,ListProduct,DetailBook,DetailCategory,DetailProduct
urlpatterns = [
   
    path('categories',ListCategory.as_view(),name='catlist'),
    path('categories/<int:pk>',DetailCategory.as_view(),name='catdet'),

    path('books',ListBook.as_view(),name='booklist'),
    path('books/<int:pk>',DetailBook.as_view(),name='bookdet'),

    path('products',ListProduct.as_view(),name='prolist'),
    path('products/<int:pk>',DetailProduct.as_view(),name='prodet'),

     path('cart',ListCart.as_view(),name='crtlist'),
    path('cart/<int:pk>',DetailCart.as_view(),name='crtdet'),

    path('',obtain_auth_token,name='obtain-auth-token'),

]
