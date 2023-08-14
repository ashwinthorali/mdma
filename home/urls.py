from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('sing-up/', views.singup, name='singup'),
    path('verify/', views.verify, name='verify'),
    path('lock/', views.lock, name='lock'),
    path('forgot-password/', views.forgotpassword, name='forgotpassword'),
    
] 
