from django.urls import path
from . import views


urlpatterns = [
		path('register/',views.register,name='register'),
		path('data/',views.data,name='f_data'),
		path('edit/<int:id>',views.edit,name='f_edit'),
		path('delete/<int:id>',views.delete,name='f_delete'),
		path('conformDelete/<int:id>',views.conformDelete,name='conformDelete'),

]