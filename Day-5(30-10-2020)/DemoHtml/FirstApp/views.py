from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req,'FirstApp/index.html')

def home(req):
	return render(req,'FirstApp/home.html')

def table(req):
	return render(req,'FirstApp/table.html')

def forms(req):
	return render(req,'FirstApp/form.html')