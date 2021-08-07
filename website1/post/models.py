from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
	postname=models.CharField(max_length=220)
	post_for=models.CharField(max_length=220)
	post_date = models.DateTimeField(auto_now_add=True)
	lastdate = models.DateTimeField('last date')

	def __str__(self):
		return str([str(self.postname),str(self.post_for),self.post_date,self.lastdate])
	

