from django.urls import path

from accounts.views import home,register,signin,signout,changepassword

urlpatterns = [
	path('',home,name="home"),

	path('register/',register,name="register"),

	path('signin/',signin,name="signin"),

	path('signout/',signout,name="signout"),

	path('changepassword/',changepassword,name="changepassword")
	]