from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
    context = {

    }
    return render(request, 'doctor/dashboard.html', context)

