from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    path('login/', views.login_page, name='login'),
path('register/', views.register_page, name='register'),
path('dashboard/', views.dashboard, name='dashboard'),
path('logout/', views.logout_page, name='logout'),

    # Modules
    path('crop/', include('crop.urls')),
    path('fertilizer/', include('fertilizer.urls')),
    path('yield_prediction/', include('yield_prediction.urls')),
    path('disease_detection/', include('disease_detection.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('history/', include('history.urls')),
    path('profile/', include('profile_app.urls')),

    # Analytics
    path('analytics/', include('analytics_app.urls')),
]