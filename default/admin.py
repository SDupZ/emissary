from django.conf import settings
from django.contrib import admin

from default.models import FAQItem

class FAQItemInline(admin.StackedInline):
    model = FAQItem
    extra = 0
