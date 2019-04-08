from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Company, Jobs, Client
from .forms import ClientForm, LeaveForm, PostJobForm, AddCompanyForm
from user_registration.models import Leave, User, netSalary
from notifications.signals import notify
from django.utils import timezone
from django.views.generic.base import View
from datetime import datetime
import notifications
from notifications.models import Notification

# Create your views here.
def home(request):
	template_name = "index.html"
	jobs = Jobs.objects.all() #queryset
	company = Company.objects.all()
	context = {'jobs':jobs,'company':company}
	return render(request, template_name, context)

def jobs(request):
	template_name = "jobs.html"
	jobs = Jobs.objects.all() #queryset
	company = Company.objects.all()
	context = {'jobs':jobs,'company':company}
	return render(request, template_name, context)

def details(request,id):
	template_name = "jobdetails.html"
	jobs = Jobs.objects.get(pk=id) #queryset
	company = Company.objects.all()
	context = {'jobs':jobs,'company':company}
	return render(request, template_name, context)

def postjob(request):
	if request.method == 'GET':
		form = PostJobForm()
		return render(request, 'postjob.html', {'form':form})
	elif request.method == 'POST':
		form = PostJobForm(request.POST, request.FILES)
		
		if form.is_valid:
			form.save()
			return redirect('/')

def addCompany(request):
	if request.method == 'GET':
		form = AddCompanyForm()
		return render(request, 'addCompany.html', {'form':form})
	elif request.method == 'POST':
		form = AddCompanyForm(request.POST)
		if form.is_valid:
			form.save()

			return redirect('/')

def apply(request, id):
	jobs = Jobs.objects.get(pk=id)
	if request.method =='POST':
		form= ClientForm(request.POST, request.FILES)
		if form.is_valid():
			client = Client()
			client.appliedjob = jobs
			client.client_name = request.POST['client_name']
			client.passport_no = request.POST['passport_no']
			client.DOB = request.POST['DOB']
			client.DOI = request.POST['DOI']
			client.DOE = request.POST['DOE']
			client.father_name = request.POST['father_name']
			client.Marital_Status = request.POST['Marital_Status']
			client.Citizenship = request.POST['Citizenship']
			client.state = request.POST['state']
			client.perm_address = request.POST['perm_address']
			client.Ref = request.POST['Ref']
			client.Contact = request.POST['Contact']
			
			client.clientimage = request.FILES['clientimage']

			client.save()

			return HttpResponse('/Request Sent/')
	else:
		form = ClientForm()

	return render(request, 'apply.html', {'form': form, 'jobs': jobs})

class review_application(View):
	
	def get(self, request, **kwargs):
		status_type = self.kwargs.get('type', None)
		pk = self.kwargs.get('id', None)
		if pk:
			Clients, selectedClient = None, Client.objects.get(pk=pk)
		else:
			if status_type=="pending":
				Clients, selectedClient = Client.objects.filter(status=0), None
			elif status_type=="processing":
				Clients, selectedClient = Client.objects.filter(status=1), None

		return render(request, 'applications.html', {'clients': Clients, 'client': selectedClient})

	def post(self, request, **kwargs):
		pk = self.kwargs.get('id', None)
	
		selectedClient = Client.objects.get(pk=pk)

		value = int(self.kwargs.get('value'))
		if int(value)==0:
			selectedClient.status = 3
		elif int(value)==1:
			if selectedClient.status==0:
				selectedClient.status=1
			elif selectedClient.status==1:
				selectedClient.status=2
		else:
			return HttpResponse('value misplaced!')
		selectedClient.save()		
		return HttpResponse("Status of the client has been changed to "+str(selectedClient.status))

def leave_request(request, id):

	staff = get_object_or_404(User, pk=id, is_staff=True)
	if request.method=='GET':
		if staff:
			if staff.leave_set.filter(status=0):
				return HttpResponse('Your request is already in pending.')
			else:
				form = LeaveForm()
				return render(request, 'leave_request.html', {'form':form, 'staff': staff})
		else:
			return HttpResponse('Access denied. Staff account required to access this section.')

	elif request.method=='POST':
		form = LeaveForm(request.POST)
		if form.is_valid():
			leave = Leave()
			leave.staff = staff
			leave.reason = request.POST.get('Reason')
			leave.startDate = request.POST.get('startDate')
			leave.endDate = request.POST.get('endDate')

			leave.save()
			notify.send(staff, recipient=User.objects.get(is_superuser=True), verb='Leave request is pending.', action_object=leave ,description=leave.reason, timestamp=timezone.now())

			return HttpResponse("Your request has been submitted.")

class leave_verification(View):
	
	def get(self, request, id):
		notification = Notification.objects.get(id=id)
		if notification.actor.is_superuser:
			staff = notification.recipient 
			
		elif not notification.actor.is_superuser:
			staff = notification.actor

		leave = notification.action_object

		if leave.status == 0:
			
			return render(request, 'leave_status.html', {'user':staff, 'leave':leave, 'no_response_yet':1})

		else:
			notification.unread = False
			notification.save()
			if leave.status == 1:
				return render(request, 'leave_status.html', {'user':staff, 'leave':leave, 'positive_response':1})

			elif leave.status == 2:
				return render(request, 'leave_status.html', {'user':staff, 'leave':leave, 'negative_response':1})	

	def post(self, request, id, value):
		
		staff = User.objects.get(pk=id)
		leave = Leave.objects.get(staff=staff, status=0)
		superuser = User.objects.get(is_superuser=True)
		
		notification = Notification.objects.filter(actor_object_id__in=id, recipient=superuser, unread=True)[0]
		
		if int(value)==0:
			verb = "Sorry, your leave request has been rejected."
			leave.status=2
			
		elif int(value)==1:
			verb = "Congratulations! Your leave request has been approved."
			if staff.leave_taken:		
				staff.leave_taken += int(str(leave.endDate-leave.startDate).split(' ')[0])+1
			else: 
				staff.leave_taken == int(str(leave.endDate-leave.startDate).split(' ')[0])+1
			leave.status=1
			
			staff.save()
		
		notification.unread = False

		notification.save()
		leave.save()

		notify.send(superuser, recipient=staff, verb=verb, action_object=leave,timestamp=timezone.now())			

		return HttpResponse('Your respone has been saved and also sent to the requesting staff via notification.')

def calculateNetSalary(request):
	employees = User.objects.filter(is_staff=True, is_superuser=False)
	for employee in employees:
		employee = employee.__dict__
		employee['net_salary_set'] = netSalary.objects.filter(employee=employee['id'])
		employee['net_salary_this_term'] = employee['Salary']*(1-employee['leave_taken']/30)

	if request.method == 'GET':
		return render(request, 'NetSalary.html', {'employees':employees})

	elif request.method == 'POST':

		if not netSalary.objects.all() or datetime.today().month>netSalary.objects.latest('pk').month or (datetime.today().month==1 and datetime.today().year==netSalary.objects.latest('pk').year+1):
			for employee in employees:
				netSal = netSalary(month=datetime.today().month, year=datetime.today().year, netSal=employee.net_salary_this_term, leave_days=employee.leave_taken)
				employee = User.objects.get(id=employee.id)
				netSal.employee = employee
				netSal.save()
				employee.leave_taken = 0
				employee.TotalSalary += netSal.netSal
				employee.save()
			
			return redirect('home')	
		else:
			return HttpResponse('Net-salary for this month has already been saved.')		

def status_check(request):
	if request.method=="GET":
		return render(request, 'statuscheck.html')

	else:
		no = request.POST.get('number')
		applications = Client.objects.filter(passport_no=no)

		if not applications:
			return HttpResponse('Sorry, no application has been found for the given passport number.')	
		else:
			return render(request, 'application_status.html', {'applications': applications})	

def about(request):
	template_name = "about-us.html"
	return render(request, template_name)

def contact(request):
	template_name = "contact-us.html"
	return render(request, template_name)

def whymarigold(request):
	template_name = "why-marigold.html"
	return render(request, template_name)

def sector(request):
	template_name = "sector-we-supply.html"
	return render(request, template_name)

def sample(request):
	template_name = "sample.html"
	return render(request, template_name)

def ourrecruitment(request):
	template_name = "our-recruitment.html"
	return render(request, template_name)

def introduction(request):
	template_name = "introduction.html"
	return render(request, template_name)

def message(request):
	template_name = "message-form-chairman.html"
	return render(request, template_name)

def chart(request):
	template_name = "organization-chart.html"
	return render(request, template_name)
