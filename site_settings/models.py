from django.db import models
from ckeditor.fields import RichTextField

class FAQPageSettings(models.Model):
    heading = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return "FAQ Page Settings"

    class Meta:
        verbose_name = "FAQ Page Settings"
        verbose_name_plural = "FAQ Page Settings"
