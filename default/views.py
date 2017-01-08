from django.shortcuts import render
from site_settings.models import FAQPageSettings, HomepageSettings
from blog.models import BlogPost
from default.forms import ContactForm

def home(request):
    template = 'index.html'

    homepage_settings = HomepageSettings.objects.all()
    homepage_settings = homepage_settings[0] if len(homepage_settings) > 0 else homepage_settings

    recent_blogs = BlogPost.objects.all().order_by('-created')[:3]
    context = {
        'homepage_settings': homepage_settings,
        'blogs': recent_blogs,
    }
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
