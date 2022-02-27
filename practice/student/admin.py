from django.contrib import admin


from .models import *

#admin.site.register(StudentInfo)

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    '''Admin View for StudentInfo'''

    list_display = ('name','standard','dob','totalMarks')
 
    ordering = ('standard',)

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    '''Admin View for contact'''

    list_display = ('name','email','phone')
   