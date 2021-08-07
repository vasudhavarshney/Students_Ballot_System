from django.shortcuts import render 
from django.http import HttpResponse 
from django.contrib.auth.models import User
from post.models import post

# Create your views here. 
def homepage(request): 
	return render(request,'post/postdetail.html',{"posts":post.objects.all(),"name":request.user}) 
