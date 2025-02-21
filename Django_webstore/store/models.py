from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20 , blank=True , null=True)
    address = models.TextField(blank=True , null=True)
    def __str__(self):
        return self.username


class Product:
    ...

class Order:
    ...

class Cart:
    ...