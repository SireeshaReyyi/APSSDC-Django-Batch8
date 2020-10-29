"""UrlsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome,name='welcome'),
    path('home/',views.home,name='home'),
    path('home1/<str:n>/',views.home1,name='home1'),
    path('rollno/<int:r>/',views.rollno,name='rollno'),
    path('data/<str:n>/<int:r>/',views.data,name='data'),
    path('htmlpage/',views.htmlpage,name='htmlpage'),
    path('htmlpage2/',views.htmlpage2,name="htmlpage2"),
]