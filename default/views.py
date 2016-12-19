from django.shortcuts import render
from site_settings.models import FAQPageSettings
from default.forms import ContactForm

def home(request):
    template = 'index.html'
    context = {}
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
            # contact_name = request.POST.get('contact_name', '')
            # contact_email = request.POST.get('contact_email', '')
            # form_content = request.POST.get('content', '')

            form.save()

    context = {
        'form': form_class,
    }
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
