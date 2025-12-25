from django.contrib import admin

from apps.users.forms import CustomAdminAuthenticationForm
from apps.users.models import User

# Register your models here.
admin.site.login_form = CustomAdminAuthenticationForm
admin.site.register(User)