from django.db import models
import datetime as dt
# Create your models here.
class result(models.Model):
   post = models.CharField(max_length=200)
   choice_text = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)
   pub_date = models.DateTimeField(default=dt.datetime.now())
   def __str__(self):
   	return self.post