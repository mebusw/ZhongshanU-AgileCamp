from django.db import models

# Create your models here.

class User(models.Model):
	_usr = models.CharField(max_length=30)
	_pwd = models.CharField(max_length=30)
	_mail = models.CharField(max_length=40)

	def _unicode_(self):
		return self._usr