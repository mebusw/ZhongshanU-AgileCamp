from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Author(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # def __unicode__(self):
    #     return self.username
    #     massage = models.CharField(max_length=200)

class Text(models.Model):
	message = models.CharField(max_length=500)

class test(models.Model):
	name = models.CharField(max_length=500)


class Daoyouxinxi(models.Model):
	name = models.CharField(max_length=500)
	# name = models.CharField(max_length=50)
	# age = models.CharField(max_length=50)
	# TEL = models.CharField(max_length=50)
	# address = models.CharField(max_length=50)
	# wantfriend = models.CharField(max_length=50)
	# money = models.CharField(max_length=50)
