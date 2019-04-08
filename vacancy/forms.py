from django import forms
from .models import Company, Jobs 

class ClientForm(forms.Form):
	client_name = forms.CharField(label='Name', max_length=100)
	passport_no = forms.CharField(label='Passport Number', max_length=10)
	DOB = forms.DateField(label='Date of Birth')
	DOI = forms.DateField(label='Date of Issue')
	DOE = forms.DateField(label='Date of Expiry')
	father_name = forms.CharField(label='Fathers Name', max_length=100)
	Marital_Status = forms.IntegerField(label='Marital Status', min_value=0, max_value=2)
	Citizenship = forms.CharField(label='Citizenship Number', max_length=30)
	state = forms.CharField(label='State', max_length=50)
	perm_address = forms.CharField(label='Permanent Address', max_length=100)
	Ref = forms.CharField(label='Referred by', max_length=100)
	Contact = forms.CharField(label='Contact Number', max_length=20)
	clientimage = forms.ImageField()

class LeaveForm(forms.Form):
	startDate = forms.DateField(label='Leave From')
	endDate = forms.DateField(label='to')

	Reason = forms.CharField(max_length=500)

class PostJobForm(forms.ModelForm):

	class Meta:
		model = Jobs
		exclude = ['listed_date']

class AddCompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = '__all__'