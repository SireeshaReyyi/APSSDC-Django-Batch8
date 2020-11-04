from django.urls import path

from.views import home,home1,register

urlpatterns = [
	path('',home,name="home"),

	path('home1/',home1,name="home1"),

	path('register/',register,name="register"),
	]