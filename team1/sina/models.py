from django.db import models

# Create your models here.

class User(models.Model):
	_usr = models.CharField(max_length=30)
	_pwd = models.CharField(max_length=30)
	_mail = models.CharField(max_length=40)

	def GetUsr(self):
		return self._usr

class Question(models.Model):
	_question = models.CharField(max_length=20000)
	_comment = models.CharField(max_length=20000)


class Guide(models.Model):
	_toWhere = models.CharField(max_length=50)
	_when = models.CharField(max_length=50)
	_peopleAmount = models.CharField(max_length=50)
	_fromWhere = models.CharField(max_length=50)
	_budget = models.CharField(max_length=50)
	_otherRequest = models.CharField(max_length=1000) 

	def GetToWhere(self):
		return self._toWhere

	def GetWhen(self):
		return self._when

	def GetPeopleAmount(self):
		return self._peopleAmount

	def GetFromWhere(self):
		return self._fromWhere

	def GetBudget(self):
		return self._budget
	
	def GetOtherRequest(self):
		return self._otherRequest
				