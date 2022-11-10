from django.contrib import admin

# Register your models here.

from .models import Deductions, Employee, Jobs

admin.site.register(Employee)
admin.site.register(Jobs)
admin.site.register(Deductions)

