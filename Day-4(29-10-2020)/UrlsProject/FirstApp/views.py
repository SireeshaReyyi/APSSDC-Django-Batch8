from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	return HttpResponse("<h1>Welcome to My Django Project</h1>")

def home(request):
	return HttpResponse("<h1>My Home Page</h1>")

def home1(request,n):
	print(type(n))
	return HttpResponse("Welcome to "+n)

def rollno(request,r):
	return HttpResponse("My Rollno is " +str(r))

def data(request,n,r):
	return HttpResponse('<h1>My Name is {} and my rollno is {}</h1>'.format(n,r))

def htmlpage(request):
	return render(request,'home.html')

def htmlpage2(request):
	return render(request,'home1.html')