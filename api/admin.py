# admin.py
from django.contrib import admin
from .models import Company, Employee  # Import the model

# Register the model
admin.site.register(Company)
admin.site.register(Employee)

