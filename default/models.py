from datetime import datetime
from django.db import models

from site_settings.models import FAQPageSettings
from ckeditor.fields import RichTextField

class FAQItem(models.Model):
    faq_settings = models.ForeignKey(FAQPageSettings, blank=True, null=True, related_name='faq_blocks')

    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(db_index=True, auto_now=True)

    question = models.CharField(blank=True, null=True, max_length=100)
    answer = RichTextField(blank=True, null=True)

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ Item"
