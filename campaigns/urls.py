from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:vacancy_id>", views.vacancy, name="vacancy"),
    path("<int:vacancy_id>/interaction", views.interaction, name="interaction")
]
