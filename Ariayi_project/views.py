from django.shortcuts import render
from projects_app.models import Project
from contactus_app.models import Footer, Message


def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        Message.objects.create(name=name, email=email, subject=subject, body=body)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()

    return render(request, 'index.html', context={'projects': projects , 'footer': footer})