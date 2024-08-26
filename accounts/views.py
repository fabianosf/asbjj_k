# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
 


''' 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('home')  
        else:
            messages.error(request, 'Credenciais inválidas')
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

'''
def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        # Verificar se o input é um email
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username  # Pega o username relacionado ao email
            except User.DoesNotExist:
                username = None
        else:
            username = username_or_email
        
        # Autenticar com username
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('home')  
        else:
            messages.error(request, 'Credenciais inválidas')
            return render(request, 'accounts/login.html', {'error': 'Credenciais inválidas'})
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para uma página após o registro
            return redirect('login')
        else:
            print(form.errors)  # Isso ajudará a depurar possíveis erros   
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})


