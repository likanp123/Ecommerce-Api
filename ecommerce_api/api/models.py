from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    inventory_count = models.IntegerField()
    source_platform = models.CharField(max_length=100)
    
class Customer(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    source_platform = models.CharField(max_length=100)
    
class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField()
    total_amount = models.FloatField()
    source_platform = models.CharField(max_length=100)