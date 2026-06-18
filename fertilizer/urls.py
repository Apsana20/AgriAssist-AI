from django.urls import path
from . import views

urlpatterns = [
    path('', views.fertilizer_form, name='fertilizer_form'),
]