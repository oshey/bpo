from django.shortcuts import render

def detail(request, **kwargs):
    return render(request, 'project/base.html')