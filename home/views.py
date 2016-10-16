from django.shortcuts import render

def front(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)
