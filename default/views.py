from django.shortcuts import render
from site_settings.models import FAQPageSettings

def home(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)

def blog(request):
    template = 'blog.html'
    context = {}
    return render(request, template, context)

def faq(request):
    template = 'faq.html'

    faqSettings = FAQPageSettings.objects.all()
    faqSettings = faqSettings[0] if len(faqSettings) > 0 else faqSettings

    context = {
        'heading': faqSettings.heading,
        'faqs': faqSettings.faq_blocks.all(),
    }
    return render(request, template, context)

def login(request):
    template = 'login.html'
    context = {}
    return render(request, template, context)

def register(request):
    template = 'register.html'
    context = {}
    return render(request, template, context)
