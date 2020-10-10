from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        "title":"Hello World!",
        "content":"Welcome to the homepage"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About page",
        "content":"Welcome to the about page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm()
    context = {
        "title":"Contact page",
        "content":"Welcome to the contact page",
        "form":contact_form
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST["full_name"])
        print(request.POST["email"])
        print(request.POST["content"])
    return render(request, "contact/view.html", context)