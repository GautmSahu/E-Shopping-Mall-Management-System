from django.db import models

class Products(models.Model):
    no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    description=models.CharField(max_length=5000)
    photo=models.ImageField(upload_to="product_images/")
    pdate=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contactno=models.IntegerField(unique=True)
    gender=models.CharField(max_length=10)
    username=models.CharField(unique=True,max_length=50)
    password=models.CharField(max_length=30)
    status=models.CharField(max_length=20,default=None)

class Admin(models.Model):
    idno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class ProductsSales(models.Model):
    idno=models.AutoField(primary_key=True)
    product_id=models.ManyToManyField(Products)
    user_id=models.ManyToManyField(Users)
    qty=models.IntegerField()
    total_bill=models.FloatField()
    purchase_date=models.DateField(auto_now_add=True)
