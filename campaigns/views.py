from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Campaign, Employee, Vacancy

# Create your views here.
def index(request):
    return render(request, "campaigns/index.html", {
        "campaigns": Vacancy.objects.all()
    })
    
    
def vacancy(request, vacancy_id):
    vacancy=Vacancy.objects.get(pk=vacancy_id)
    return render(request, "campaigns/vacancies.html",{
      "vacancy": vacancy,
      "employees": vacancy.employees.all(),
      
    })
    
    
def interaction(request, vacancy_id):
    if request.method == "POST":
        vacancy=Vacancy.objects.get(pk=vacancy_id)
        emloyee_id=int(request.POST["employee"])
        employee=Employee.objects.get(pk=emloyee_id)
        employee.vacancies.add(vacancy) 
        return HttpResponseRedirect(reverse("vacancy", args=(vacancy.id)))   