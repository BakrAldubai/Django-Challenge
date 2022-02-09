from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):

    name = models.CharField(max_length=255,unique=True)
    origin = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', default='images/default.png',blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'brands/{self.id}'


class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    kind = models.CharField(max_length=100)
    description = models.TextField(blank=True,default='')
    expir_date = models.DateField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',default='images/default.png',blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'products/{self.id}'


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True,unique=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Accepted','Accepted'),
        ('Waiting','Waiting'),
        ('Not Accepted','Not Accepted'))

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS , default='Accepted')
    pieces = models.IntegerField(default=0 )

    def __str__(self):
        return self.product.name















