# from django.forms import ModelForm
from .models import library
from django import forms


class LibraryForm(forms.ModelForm):
	class Meta:
		model = library
		fields = '__all__'


		widgets = {

		'book_name' : forms.TextInput(attrs={'class':'form-control'}),
		'book_no' : forms.NumberInput(attrs={'class':'form-control'}),
		'author' : forms.TextInput(attrs={'class':'form-control'}),
		'department' : forms.Select(attrs={'class':'form-control'}),
		'publication_date' : forms.DateInput(attrs={'class':'form-control'}),
		
		}

