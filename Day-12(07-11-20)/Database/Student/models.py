from django.db import models

# Create your models here.
class student_data(models.Model):
	First_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=20)
	Age = models.IntegerField(null=True,blank=True)
	Email = models.EmailField(unique=True)
	phone = models.IntegerField(help_text = "Enter your 10 digit mobile number")


	def __str__(self):
		return self.First_Name +' '+ self.Last_Name


class library(models.Model):
	branches = (
			('ece','ece'),
			('cse','cse'),
			('it','it'),
			('civil','civil'),
			('mech','mech'),
			('chem','chem'),
			('mme','mme')
		)

	book_name = models.CharField(max_length=50)
	book_no = models.IntegerField()
	author = models.CharField(max_length=40)
	department = models.CharField(max_length=10,choices = branches )
	publication_date = models.DateField(help_text='format : yyyy-mm-dd')

	def __str__(self):
		return self.book_name + ' ' + self.author