from django.contrib import admin
from .models import Campaign, Vacancy, Employee

# Register your models here.
class VacancyAdmin(admin.ModelAdmin):
    list_displey = ("id", "employer", "requirements", "role")
    
   

admin.site.register(Campaign)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Employee)