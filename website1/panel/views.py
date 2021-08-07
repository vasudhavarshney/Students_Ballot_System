from django.shortcuts import render 
from django.http import HttpResponse 
from django.contrib.auth.models import User
from .models import result


# Create your views here. 
def panelview(request): 
	return render(request,'panel/paneldetails.html',{"name":request.user}) 

def resultupdate(request):
	current_post = result.objects.order_by('post')[:5]
	context = {'current_post': current_post}
	return render(request, 'pages/resultupdate.html', context)