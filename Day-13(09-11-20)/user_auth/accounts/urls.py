from django.urls import path

from accounts.views import home

urlpatterns = [
	path('',home,name="home"),
	]