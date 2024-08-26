from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages


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






