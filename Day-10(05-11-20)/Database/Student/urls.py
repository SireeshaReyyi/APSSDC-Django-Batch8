from django.urls import path
from . import views


urlpatterns = [
		path('',views.home,name='home'),
		path('register/',views.register,name='register'),
		path('data/',views.data,name='data'),
		path('edit/<int:id>',views.edit,name='edit'),
		path('delete/<int:id>',views.delete,name='delete')
]


