from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_form, name='crop_form'),
]