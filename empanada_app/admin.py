from django.contrib import admin
from .models import Empanada

# Register your models here.

@admin.register(Empanada)
class EmpanadasAdmin(admin.ModelAdmin):
    ...