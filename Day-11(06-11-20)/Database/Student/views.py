from django.shortcuts import render,redirect
from .models import student_data
from django.http import HttpResponse
# Create your views here.



def home(request):
	return render(request, 'student/home.html')
def register(request):
	if request.method=='POST':

		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		age = request.POST.get('age')
		email = request.POST.get('mail')
		phone = request.POST.get('phone')

		student_data.objects.create(First_Name=fname,Last_Name=lname,Age=age,Email=email,phone=phone)

		# return HttpResponse("Registration Successful")
		return redirect('data')
	return render(request,'student/register.html')


def data(request):
	data = student_data.objects.all()
	return render(request,'student/data.html',{'data':data})


def edit(request,id):
	data = student_data.objects.get(id=id)
	if request.method=='POST':
		data.First_Name = request.POST.get('fname')
		data.Last_Name = request.POST.get('lname')
		data.Age = request.POST.get('age')
		data.Email = request.POST.get('mail')
		data.phone = request.POST.get('phone')
		data.save()
		return redirect('data')

	return render(request,'student/edit.html',{'data':data})

def delete(request,id):
	data = student_data.objects.get(id=id)
	data.delete()
	return redirect('data')
