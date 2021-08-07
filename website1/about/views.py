from django.shortcuts import render 
from django.http import HttpResponse 
from django.contrib.auth.models import User


# Create your views here. 
def about(request): 
	return render(request,'about/aboutdetails.html',{"name":request.user}) 
