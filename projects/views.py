from django.shortcuts import render, get_object_or_404

from .models import Project


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_details.html', {'project': project})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})
