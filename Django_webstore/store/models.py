from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20 , blank=True , null=True)
    address = models.TextField(blank=True , null=True)
    def __str__(self):
        return self.username


class Product(models.Model):

    def __str__(self):
        return self.name
    
    PRODUCT_CATEGORY = [('Laptop', 'لپ تاپ'),
                ('SmartPhone', 'گوشی هوشمند'),
                ('Tablet' , 'تبلت'),
                ('SmartWatch' , 'ساعت هوشمند'),
                ('Accessories' , 'لوازم جانبی')]
    
    name = models.CharField(max_length=100, default=None)
    brand = models.CharField(max_length=100 , default=None)
    price = models.DecimalField(max_digits=15 , decimal_places=3 , default=None)
    info = models.TextField(default=None)
    stock = models.PositiveIntegerField(default=None) # if less than x : only 1 item has been remain
    category = models.CharField(max_length=50 , choices=PRODUCT_CATEGORY , default=None)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/img/' , default=None)
    product = models.ForeignKey(Product , related_name="images" , on_delete=models.CASCADE) # Cascade signifies that if a product is deleted, then its photos are also deleted.
    def __str__(self):
        return f"Image for {self.product.name}"


class comment:  
    ...

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2 , default=None)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)