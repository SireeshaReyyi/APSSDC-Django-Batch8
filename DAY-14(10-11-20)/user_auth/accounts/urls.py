from django.urls import path

from accounts.views import home,register,signin

urlpatterns = [
	path('',home,name="home"),

	path('register/',register,name="register"),

	path('signin/',signin,name="signin"),
	]