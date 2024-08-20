from django.shortcuts import render

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def class_(request):
    return render(request, "core/class.html")

def schedule(request):
    return render(request, "core/schedule.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]                      
            mensagem = form.cleaned_data["mensagem"]

            # Enviar o email
            send_mail(
                f"Mensagem de {nome}",  # Assunto do email
                mensagem,  # Mensagem
                email,  # De (quem enviou)                
                ["fabiano.freitas@gmail.com"],  # Para (seu email)
            )

            return HttpResponse("Obrigado pelo contato!")
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})

def footer(request):
    return render(request, "core/footer.html")


def modal(request):
    return render(request, "core/modal.html")


