"""hrms URL Configuration"""

from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

from user_registration import urls
from vacancy.views import *
urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^jobs', jobs, name='jobs'),
    url(r'^about', about, name='about'),
    url(r'^contact', contact, name='contact'),
    url(r'^whymarigold', whymarigold, name='whymarigold'),
    url(r'^sector', sector, name='sector'),
    url(r'^sample', sample, name='sample'),
    url(r'^ourrecruitment', ourrecruitment, name='ourrecruitment'),
    url(r'^introduction', introduction, name='introduction'),
    url(r'^message', message, name='message'),
    url(r'^chart', chart, name='chart'),
    path('job/<id>/apply/', apply, name='apply'),
    path('job/addnew/', postjob, name='postjob'),
    path('addCompany/', addCompany, name='addCompany'),
    path('accounts/', include('user_registration.urls')),
    path('details/<id>', details, name='details'),
    path('leave_request/staff/<id>', leave_request, name='leave'),
    path('leave_status/notification/<id>', leave_verification.as_view(), name='leave_status'),
    path('leave_response/staff/<id>/value/<value>', leave_verification.as_view(), name='leave_verify'),
    path('netSalary/allEmployees/', calculateNetSalary, name='netsalary'),

    path('applications/<type>/', review_application.as_view(), name='all_app'),
    url(r'^application/details/(?P<id>[0-9]+)/$', review_application.as_view(), name='specific_app'),
    path('application/<id>/value/<value>', review_application.as_view(), name='process'),
    path('application/statuscheck/', status_check, name='appstatus' ),
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),

]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
