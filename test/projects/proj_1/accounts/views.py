from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']  # Ensure consistency

        user = auth.authenticate(username=username, password=password1)  # Fixed typo

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')  # Fixed typo
                return redirect('register')
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            print('User created')
            return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')  # Provide feedback
            return redirect('register')
    else:
        return render(request, 'register.html')
