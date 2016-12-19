from django.forms import ModelForm
from default.models import ContactMessage


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['contact_name', 'contact_email', 'content']
