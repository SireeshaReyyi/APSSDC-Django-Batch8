from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .models import UserProfile

from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'accounts/home.html')


def register(request):
	if request.method=="POST":
		fname=request.POST.get('first_name')
		lname=request.POST.get('last_name')
		uname=request.POST.get('username')
		em=request.POST.get('email')
		im=request.FILES.get('image')
		pwd=request.POST.get('password')
		user=User.objects.create_user(first_name=fname,
			last_name=lname,username=uname,email=em,password=pwd)
		UserProfile.objects.create(user=user,image=im)
		messages.success(request,'%s is successully Registerd..!'%(uname))
		return redirect('signin')
	return render(request,'accounts/register.html')


def signin(request):
	return render(request,'accounts/signin.html')