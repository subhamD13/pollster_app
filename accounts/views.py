from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'User name already taken...')
                return redirect('/accounts/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Sorry! Email already taken...')
                return redirect('/accounts/register/')

            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, 
                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/accounts/login')
            
        else:
            messages.info(request, 'Sorry! Password not matching....')
            return redirect('/accounts/register/')
        
        return redirect('/')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid User...')
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')