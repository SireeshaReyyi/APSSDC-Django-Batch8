from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req,'FirstApp/index.html')

def home(req):
	return render(req,'FirstApp/home.html')

def table(req):
	return render(req,'FirstApp/table.html')

def forms(req):
	if req.method=='POST':
		uname=req.POST['name']
		uemail=req.POST['email']
		udob=req.POST['dob']
		ubranch=req.POST['branch']
		ugender=req.POST['gender']
		return render(req,'FirstApp/output.html',{'uname':uname,
			'uemail':uemail,'udob':udob,'ubranch':ubranch,'ugender':ugender})
	return render(req,'FirstApp/form.html')

def names(req,n):
	return render(req,'FirstApp/names.html',{'name':n})

def number(req,num):
	data=[]
	for i in range(1,num+1):
		data.append(i)

	return render(req,'FirstApp/numbers.html',{'data':data})