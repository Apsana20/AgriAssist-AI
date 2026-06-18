from django.urls import path
from . import views

urlpatterns = [
    path('', views.yield_form, name='yield_form'),
]