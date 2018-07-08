from django.db import models

# Create your models here.

class Yore(models.Model):
	yore = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.yore

class Word(models.Model):
	yore = models.ForeignKey(Yore)
	word = models.CharField(max_length=68, unique=True)
	meaning = models.TextField()
	date = models.DateField()
	
	def __str__(self):
		return self.word