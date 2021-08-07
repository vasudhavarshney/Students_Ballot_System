from django.db import models

# Create your models here.
class applicant(models.Model):
	candidate_name=models.CharField(max_length=200)
	year =models.CharField(max_length=200)
	post=models.CharField(max_length=200)



	def __str__(self):
		return self.candidate_name