from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

import requests
from django.http import StreamingHttpResponse
from django.contrib.auth.views import login_required

#@login_required
def download(request):
    # handle user custom user permissions
    url = 'file_url_here'
    filename = os.path.basename(url)
    r = requests.get(url, stream=True)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Disposition'] = f'attachement; filename="{filename}"'
    return response


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

