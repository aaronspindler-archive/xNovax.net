from django.shortcuts import render, get_object_or_404
from .models import Blog

def detail(request, pk):
    detailblog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html',{'blog':detailblog})
