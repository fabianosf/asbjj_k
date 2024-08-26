from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages

from contact.forms import ContactForm


def home(request):
    context = {
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, "core/home.html", context)

def about(request):
    return render(request, "core/about.html")

def class_(request):
    return render(request, "core/class.html")

def schedule(request):
    return render(request, "core/schedule.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Pega os dados do formulário
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']            
            # Envia o e-mail
            send_mail(
                f'Novo envio de formulario {name}',
                f'Mensagem:\n{message}\n\nContato Detalhes:\nNome: {name}\nEmail: {email}\nTelefone: {phone}',
                email,  # Envia o e-mail a partir do e-mail do remetente
                ['fabiano.freitas@gmail.com'],  # Substitua pelo seu e-mail
            )
            messages.success(request, 'Sua mensagem foi enviada com sucesso !!!')
            form = ContactForm()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})






