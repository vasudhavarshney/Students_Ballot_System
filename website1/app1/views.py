from django.shortcuts import render 
from django.http import HttpResponse 
from django.contrib.auth.models import User
from post.models import post

# Create your views here. 
def homepage(request): 
	if request.user.is_staff == True:
		return render(request,'app1/main1.html',{"name":request.user}) 
	else:
		return render(request,'app1/main.html',{"name":request.user}) 



