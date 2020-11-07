from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import faculty_data
from .forms import facultyForm


# Create your views here.
def register(req):
	form = facultyForm()
	if req.method=='POST':
		form = facultyForm(req.POST)
		form.save()
		return HttpResponse("Successful :)")
	return render(req,'faculty/register.html',{'form':form})


def data(request):
	data = faculty_data.objects.all()
	return render(request,'faculty/data.html',{'data':data})


def edit(request,id):
	data = faculty_data.objects.get(id=id)
	form = facultyForm(instance=data)
	if request.method=='POST':
		form = facultyForm(request.POST,instance=data)
		form.save()
		return redirect('f_data')
	return render(request,'faculty/edit.html',{'form':form,'id':id})


def delete(request,id):
	data = faculty_data.objects.get(id=id)
	return render(request,'faculty/delete.html',{'data':data})

def conformDelete(request,id):
	data = faculty_data.objects.get(id=id)
	data.delete()
	return redirect('f_data')

