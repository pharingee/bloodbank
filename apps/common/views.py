from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from models import Event


def home(request):
    return render(request, 'index.html')


def user_login(request):
    errors = {'errors': []}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                errors = {
                    'errors': ['User has been disabled']
                }
        else:
            errors = {
                'errors': ['Invalid email or password']
            }

        return render(request, 'dashboard/login.html', errors)

    return render(request, 'dashboard/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'dashboard/login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')


def info(request):
    return render(request, 'info.html')


def events(request):
    events = Event.objects.filter(is_visible=True)
    return render(request, 'events.html', {'events': events})
