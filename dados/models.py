from django.db import models
# from igreja.models import *

class dado(models.Model):

	Nome = models.TextField()
	Congergacao = models.ForeignKey('congregacao' , on_delete=models.CASCADE)

class congregacao(models.Model):

	Nome = models.CharField(max_length=15)