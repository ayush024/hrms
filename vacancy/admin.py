from django.contrib import admin
from .models import Company, Jobs, Client
# Register your models here.
admin.site.register(Company)
admin.site.register(Jobs)
admin.site.register(Client)