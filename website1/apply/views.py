from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from .forms import applicantForm
from django.contrib import messages
from .models import applicant
# Create your views here. 
def application(request): 
	if request.method == 'POST': 
		form = applicantForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('candidate_name')  # Grab the username that is submitted for now
			messages.success(request, f'Account created for {username}!')
			return redirect('/apply')
	else:
		form = applicantForm()
	return render(request,'apply/applicationdetails.html',{'form':form}) 





def userinfo(request): 

	return render(request,'apply/aspirantinfo.html',{"applicants":applicant.objects.all(),"user":request.user,"name":request.user}) 
