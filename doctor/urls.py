from django.urls import path
from . import views
app_name='doctor'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
] 
