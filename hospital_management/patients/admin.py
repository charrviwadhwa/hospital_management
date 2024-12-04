from django.contrib import admin
from .models import Patient

# Customize the display of the Patient model in the Django Admin interface
class PatientAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('pid', 'pname', 'gender', 'fee', 'age', 'ward', 'disease')
    
    # Add filters on the right side for easy filtering of records
    list_filter = ('gender', 'ward', 'disease')
    
    # Make some fields searchable in the admin search bar
    search_fields = ('pname', 'disease', 'ward')
    
    # Add options for ordering the records in the admin panel
    ordering = ('pid',)  # This will order by ID in ascending order by default

    # Add functionality to allow editing of fields directly in the list view
    list_editable = ('fee', 'age', 'ward')  # Allows editing fee, age, and ward directly in the list view

    # You can also define how the model's form will appear in the Django admin
    # fieldsets organize the form into sections with labels and fields
    fieldsets = (
        (None, {
            'fields': ('pname', 'gender', 'fee', 'age', 'ward', 'disease')
        }),
    )

# Register the Patient model with the PatientAdmin customization
admin.site.register(Patient, PatientAdmin)
