from django.shortcuts import render
from site_settings.models import FAQPageSettings, HomepageSettings
from default.forms import ContactForm

def home(request):
    template = 'index.html'

    homepage_settings = HomepageSettings.objects.all()
    homepage_settings = homepage_settings[0] if len(homepage_settings) > 0 else homepage_settings

    context = {
        'homepage_settings': homepage_settings,
    }
    return render(request, template, context)

def blog(request):
    template = 'blog.html'
    context = {}
    return render(request, template, context)

def contact(request):
    template = 'contact.html'
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form': form_class,
    }
    return render(request, template, context)

def faq(request):
    template = 'faq.html'

    faq_settings = FAQPageSettings.objects.all()
    faq_settings = faq_settings[0] if len(faq_settings) > 0 else faq_settings

    context = {
        'heading': faq_settings.heading,
        'faqs': faq_settings.faq_blocks.all(),
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
