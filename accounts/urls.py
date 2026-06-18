from django.urls import path
from .views import home, login_page, register_page, dashboard, logout_page
urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_page, name='logout'),
]