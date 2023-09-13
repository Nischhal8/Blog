from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(post)

from django.contrib import admin
admin.site.login_template = "blog/login.html"