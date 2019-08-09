from django.shortcuts import render, get_object_or_404
from .models import Course

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_details.html', {'course':course})
