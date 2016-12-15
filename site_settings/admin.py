from django.conf import settings
from django.contrib import admin

from site_settings.models import FAQPageSettings
from default.admin import FAQItemInline

class FAQPageSettingsAdmin(admin.ModelAdmin):
    inlines = [FAQItemInline]

admin.site.register(FAQPageSettings, FAQPageSettingsAdmin)
