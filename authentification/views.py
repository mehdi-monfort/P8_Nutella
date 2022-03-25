from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return HttpResponse("Cet ensemble nom/password n'est pas enregistrer")
        login(request, user)
        return redirect('/')
    else:
        form = UserForm()
        return render(request, 'authentification/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == "POST":
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            newuser = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email
            )
            newuser.save()
        except IntegrityError:
            return HttpResponse("Ce nom d'utilisateur est déjà pris")

    else:
        form = UserRegistrationForm()
        return render(request, 'authentification/signup.html', {'form': form})
    return HttpResponse("Vous êtes bien enregistrer")
