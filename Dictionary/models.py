from django.db import models

# Create your models here.

class Word(models.Model):
	word = models.CharField(max_length=68, unique=True)
	meaning = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.word