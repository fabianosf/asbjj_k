from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def class_(request):
    return render(request, "core/class.html")

def schedule(request):
    return render(request, "core/schedule.html")


def contact(request):
    return render(request, "core/contact.html")


def footer(request):
    return render(request, "core/footer.html")


def modal(request):
    return render(request, "core/modal.html")


