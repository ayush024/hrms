from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.http import Http404, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from user_registration.tokens import account_activation_token
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.contrib import messages
from .models import User, UserProfile, employeeKey
from .forms import UserSignupForm, UserLoginForm
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import user_passes_test, login_required
from datetime import datetime
import random
import os

def send_template_email(subject, body, to_email, from_email=settings.EMAIL_HOST_USER):

	email = EmailMultiAlternatives(subject, body, settings.EMAIL_HOST_USER , [to_email])
	email.content_subtype='html'
	email.mixed_subtype = 'related'	
	email.send()

class Homepage(TemplateView):
	template_name='index.html'

def logout_view(request):
	logout(request)
	return redirect('/')

class AccountActivationRedirect(TemplateView):
	template_name = 'user_registration/account_activation_notice.html'

class UserSignupView(View):

	form_class = UserSignupForm
	template_name = 'user_registration/signup.html'

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('/')
		form = self.form_class(None)
		context={
		'form':form
		}
		return render(request, self.template_name, context)


	def post(self, request):

		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = form.cleaned_data['username']
			user.email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			user.set_password(password)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate Your account'
			template_message = render_to_string('user_registration/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': (user.pk),
				'token': account_activation_token.make_token(user),
				})
			try:
				send_template_email(subject=subject, body=template_message, to_email=user.email)
			except:
				messages.error(request, "Something went wrong. Please try again.")
				user.delete()
				return redirect('signup')
#				return HttpResponse(form.error())

			return redirect('account-activation')

		return render(request, self.template_name, {'form': form})

def activate(request, uidb64, token):
	if request.user.is_authenticated:
			logout(request)
	try:
		user = User.objects.get(pk=uidb64)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.email_confirmed = True

		user.save()
		return redirect('login')
	else:
		raise Http404

class UserLoginView(View):

	form_class = UserLoginForm
	template_name = 'user_registration/login.html'

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('/')
		form = self.form_class(None)
		return render(request, self.template_name,{'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(email=user_email, password=password)
			if user is not None:
				#to check if disabled or banned status
				if user.is_active:
					login(request, user)
					return redirect('/')
		messages.error(request,'Login Failed! Please Try Again...')
		return render(request, self.template_name, {'form':form})

@login_required
def StaffSignupView(request, id):
	if request.method=="GET":
		return render(request, 'staffsignup.html')

	else:
		key = request.POST.get('key')
		latest_key = employeeKey.objects.last()
		if key==latest_key.key:
			user.is_staff = True
			user.Salary = 0
			user.leave_taken = 0
			user.TotalSalary = 0
			user.attendance = 0
			user.save()

			return HttpResponse("Thankyou for using staff account. You can start using your account by going back and refreshing.")

		else:
			return HttpResponse("Sorry, key doesn't match")

@user_passes_test(lambda u: u.is_superuser)
def createKey(request):
	if request.method=="GET":
		current_key = employeeKey.objects.last()
		return render(request, 'change_key.html', {'current_key':current_key})
	else:
		key = request.POST.get('key')
		new_key = employeeKey(key=key)
		new_key.save()
		return HttpResponse("StaffSignup key has been changed successfully")

def generate(request):
	if request.method=="POST":
		key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(20)])
		new_key = employeeKey(key=key)
		new_key.save()
		return HttpResponse('StaffSignup key changed successfully!')
	else:
		return HttpResponse('Access Denied!')