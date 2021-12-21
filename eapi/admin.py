from django.contrib import admin
from .models import BookModel, Cart,CategoryModel,ProductModel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(Cart)