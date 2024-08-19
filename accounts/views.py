# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages

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

def logout_view(request):
    logout(request)
    return redirect('login')  

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para uma página após o registro
            return redirect('home')  # Altere 'pagina_de_sucesso' para a URL desejada após o registro
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def some_protected_view(request):
    return render(request, 'accounts/protected.html')