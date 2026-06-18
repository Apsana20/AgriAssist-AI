from django.urls import path
from . import views

urlpatterns = [
    path('', views.disease_form, name='disease_form'),
]