from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import *

urlpatterns = [

    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/', AccountActivationRedirect.as_view(), name = 'account-activation'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
    path('signup_as_staff/user/<id>', StaffSignupView, name='staffsignup'),
    path('change_key/', createKey, name='change_key'),
    path('random_keygen/', generate, name='generate'),
]

