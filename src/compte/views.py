from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('profil')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été créé avec succès')
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form}) 

def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'profil.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profil')
        else:
            messages.info(request, "Nom d'utilisateur et/ou mot de passe incorrects")
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profil_view(request):
    return render(request, 'profil.html')