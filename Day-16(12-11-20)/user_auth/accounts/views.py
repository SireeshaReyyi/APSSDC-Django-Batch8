from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .models import UserProfile

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from user_auth import settings

from django.core.mail import send_mail


from .forms import UserUpdateForm,ProfileUpateForm


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
		#sub="UserLogins"
		# body="Welcome to Our project\n This is your username:- "+uname+'\n This is your password:-  '+pwd
		# receiver=em
		# sender=settings.EMAIL_HOST_USER
		# send_mail(sub,body,sender,[receiver])
		# messages.success(request,'account has been succesfully created check your mail to check login credentials')
		messages.success(request,'successfully regisred...!')
		return redirect('signin')
	return render(request,'accounts/register.html')


def signin(request):
	if request.method=="POST":
		uname=request.POST.get('uname')
		pwd=request.POST.get('pswd')
		user=authenticate(username=uname,password=pwd)
		if user:
			login(request,user)
			messages.success(request,'%s is successully logged..!'%(uname))
			return redirect('/')
		else:
			messages.error(request,'invalid username or password')
			return render(request,'accounts/signin.html')
	return render(request,'accounts/signin.html')


def signout(request):
	logout(request)
	return redirect('signin')


def changepassword(request):
	if request.method=="POST":
		old=request.POST.get('oldpwd')
		new=request.POST.get('newpwd')
		con=request.POST.get('conpwd')
		if new == con:
			user=User.objects.get(username__exact=request.user.username)
			user.set_password(new)
			user.save()
			messages.info(request,'password changed successfully..!')
			return redirect('/')
		else:
			messages.dubug(request,"password doesn't match")
			return render(request,'accounts/changepassword.html')

	return render(request,'accounts/changepassword.html')


def myprofile(request):
	user=User.objects.get(id=request.user.id)
	pro=UserProfile.objects.get(user=user)
	context={'user':user,'pro':pro}
	return render(request,'accounts/myprofile.html',context)


def updateprofile(request):
	user=User.objects.get(id=request.user.id)
	pro=UserProfile.objects.get(user=user)
	if request.method=="POST":
		uform=UserUpdateForm(request.POST,instance=request.user)
		pform=ProfileUpateForm(request.POST,request.FILES,instance=request.user.userprofile)
		if uform.is_valid() and pform.is_valid():
			uform.save()
			pform.save()
			messages.info(request,'profile is updated successfully..!')
			return redirect('myprofile')
		else:
			messages.error(request,'profile not updated..!')
			uform=UserUpdateForm(instance=user)
			pform=ProfileUpateForm(instance=pro)
			context={'uform':uform,'pform':pform}
			return render(request,'accounts/updateprofile.html',context)
	else:		
		uform=UserUpdateForm(instance=user)
		pform=ProfileUpateForm(instance=pro)
		context={'uform':uform,'pform':pform}
		return render(request,'accounts/updateprofile.html',context)