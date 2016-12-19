from django.conf import settings
from django.contrib import admin

from default.models import FAQItem, ContactMessage

class FAQItemInline(admin.StackedInline):
    model = FAQItem
    extra = 0


admin.site.register(ContactMessage)
