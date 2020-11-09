from django import forms
from .models import faculty_data


class facultyForm(forms.ModelForm):
	class Meta:
		model = faculty_data
		# fields = ['firstname','lastname','email']
		fields = '__all__'
