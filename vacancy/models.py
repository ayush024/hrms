from django.db import models

# Create your models here.
class Company(models.Model):
	Name= models.CharField(max_length=50)
	Type = models.CharField(max_length=50)
	Location = models.CharField(max_length=50)

	def __str__(self):
		return self.Name

class Jobs(models.Model):
	companyjobs = models.ForeignKey(Company, related_name='job', on_delete=models.CASCADE)
	title=models.CharField(max_length=50)
	location = models.CharField(max_length=100)	
	salary = models.IntegerField(default=0)
	qualifications = models.CharField(max_length=500)
	fooding = models.BooleanField(default=0)
	lodging = models.BooleanField(default=0)
	insurance = models.BooleanField(default=0)
	listed_date = models.DateField(auto_now=True)
	last_date = models.DateField()
	time_period = models.IntegerField(default=0)
	image = models.ImageField(upload_to='Vacancies/Image/%Y/%m/%d/', null=True)

	def __str__(self):
		return self.title

class Client(models.Model):
	appliedjob = models.ForeignKey(Jobs, related_name='applied', on_delete=models.SET_NULL, null=True)
	client_name = models.CharField(max_length=100)
	passport_no = models.CharField(max_length=10)
	DOB = models.DateField()
	DOI = models.DateField()
	DOE = models.DateField()
	father_name = models.CharField(max_length=100)
	Marital_Status = models.IntegerField()
	Citizenship = models.CharField(max_length=30)
	state = models.CharField(max_length=50)

	perm_address = models.CharField(max_length=100)
	Ref = models.CharField(max_length=100)
	Contact = models.CharField(max_length=20)
	clientimage = models.ImageField(null=True)
	status = models.IntegerField(default=0)
	def __str__(self):
		return self.client_name
