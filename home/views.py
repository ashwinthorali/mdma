from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'auth/login.html', context)


def singup(request):
    context = {

    }
    return render(request, 'auth/singup.html', context)

def verify(request):
    context = {

    }
    return render(request, 'auth/verification.html', context)


def lock(request):
    context = {

    }
    return render(request, 'auth/lock.html', context)


def forgotpassword(request):
    context = {

    }
    return render(request, 'auth/forgot_password.html', context)