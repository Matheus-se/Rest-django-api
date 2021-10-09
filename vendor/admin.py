from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Vendor

admin.site.register(Vendor, auth_admin.UserAdmin)