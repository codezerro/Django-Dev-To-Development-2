from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "log in")
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "not login")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "The user name already taken")
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "The email name already taken")
                    return redirect('accounts:register')
                else:
                    # looks good
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    # auth.login(request, user)
                    # messages.success(request, "You are now loged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request, "You are now loged in")
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

    return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.error(request, 'you are logout')
    return redirect('pages:index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
