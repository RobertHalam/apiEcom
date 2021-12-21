from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class BookModel(models.Model):
    title = models.CharField(max_length=30)

    category = models.ForeignKey(CategoryModel,related_name='booksmodel',on_delete=models.CASCADE)
    
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    desctiption = models.TextField()
    imgurl=models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title


class ProductModel(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    category = models.ForeignKey(CategoryModel,related_name='productsmodel',on_delete=models.CASCADE)
    
    price = models.IntegerField()
    stock = models.IntegerField()
    desctiption = models.TextField()
    imgurl=models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)


class Cart(models.Model):
    cart_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    
    date_created = models.DateField(auto_now_add=True)

    books = models.ManyToManyField(BookModel)
    product = models.ManyToManyField(ProductModel)


    class Meta:
        ordering = ['cart_id','-date_created']
    
    def __str__(self):
        return f'{self.cart_id}'