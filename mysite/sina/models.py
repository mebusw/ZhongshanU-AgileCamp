# coding: UTF-8
from django.db import models

# Create your models here.

class Placename(models.Model):
	"""
	存有地名的类
	"""

	name = models.CharField(max_length = 3000 )

	def __str__(self):
		return self.name