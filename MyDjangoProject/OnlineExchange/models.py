from django.db import models

# Create your models here.


class User(models.Model):
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    mail = models.CharField(max_length=20)
    uid = models.IntegerField(primary_key=True)


class Product(models.Model):
    uid = models.IntegerField()
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    date = models.DateField()
    status = models.IntegerField()
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
