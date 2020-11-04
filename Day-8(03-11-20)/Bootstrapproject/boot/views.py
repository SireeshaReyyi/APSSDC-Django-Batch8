from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'boot/home.html')


def home1(request):
	return render(request,'boot/home1.html')


def register(request):
	return render(request,'boot/register.html')
