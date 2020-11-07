from django.db import models

# Create your models here.



class faculty_data(models.Model):
	branches = (
			('ece','ECE'),
			('cse','CSE'),
			('it','IT'),
			('mech','MECH'),
			('civil','CIVIL')
		)

	firstname  = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	facultyid = models.CharField(max_length=20)
	department = models.CharField(max_length=6,choices=branches)
	email = models.EmailField()
	phone = models.IntegerField()


	def __str__(self):
		return self.firstname