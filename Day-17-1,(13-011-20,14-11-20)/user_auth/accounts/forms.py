from django.forms import ModelForm

from django.contrib.auth.models import User

from.models import UserProfile


from django.contrib.auth.forms import UserCreationForm



class UserRegister(UserCreationForm):
	class Meta():

		model=User
		fields=['first_name','last_name','username','email']



class UserUpdateForm(ModelForm):
	class Meta():

		model=User

		fields=['first_name','last_name','username','email']

class ProfileUpateForm(ModelForm):
	class Meta():

		model=UserProfile

		fields=['image','gender','dob','mobileno','address']
			




