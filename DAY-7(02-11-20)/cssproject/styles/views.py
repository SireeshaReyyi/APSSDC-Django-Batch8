from django.shortcuts import render

# Create your views here.



def home(request):
	return render(request,'styles/home.html')



def login(request):
	return render(request,'styles/login.html')

