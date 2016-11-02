from django.shortcuts import render

def home(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)

def blog(request):
    template = 'blog.html'
    context = {}
    return render(request, template, context)

def login(request):
    template = 'login.html'
    context = {}
    return render(request, template, context)

def register(request):
    template = 'register.html'
    context = {}
    return render(request, template, context)
