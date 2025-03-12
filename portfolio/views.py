from django.shortcuts import render
from .models import Project, Testimonial

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})

def project(request, id):
    project = Project.objects.get(id=id)
    print(project)
    return render(request, 'portfolio/project-details.html', {'project': project})