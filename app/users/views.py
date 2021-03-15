from django.shortcuts import render

def login(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, "You are successfully loged in!")
            auth.login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid username or password")

    return render(request, 'users/login.html')

def logout(request):
    """Logout view."""
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'You are successfully loged out')
    return redirect('login')