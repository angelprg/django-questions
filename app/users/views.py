from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages


def login(request):
    """Login view."""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            messages.success(request, "Ha iniciado sesión correctamente")
            auth.login(request, user)
            return redirect('questions')
        messages.error(request, "Email o contraseña inválidos")

    return render(request, 'users/login.html')


def logout(request):
    """Logout view."""
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')
