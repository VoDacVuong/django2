from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    phone = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    salary = models.IntegerField(default=0)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)

