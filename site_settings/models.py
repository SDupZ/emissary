from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from ckeditor.fields import RichTextField


class HomepageSettings(models.Model):
    main_heading = models.CharField(max_length=100, blank=True)
    main_subtitle = models.CharField(max_length=100, blank=True)
    main_image = FilerImageField(blank=True, null=True, related_name="jumbotron_header_image")

    leaving_soon_heading = models.CharField(max_length=100, blank=True)

    services_heading_one = models.CharField(max_length=100, blank=True)
    services_blurb_one = models.TextField(max_length=150, blank=True)
    services_image_one = FilerImageField(blank=True, null=True, related_name="services_image_one")

    services_heading_two = models.CharField(max_length=100, blank=True)
    services_blurb_two = models.TextField(max_length=150, blank=True)
    services_image_two = FilerImageField(blank=True, null=True, related_name="services_image_two")

    services_heading_three = models.CharField(max_length=100, blank=True)
    services_blurb_three = models.TextField(max_length=150, blank=True)
    services_image_three = FilerImageField(blank=True, null=True, related_name="services_image_three")

    video = models.URLField(max_length=200)

    news_heading = models.CharField(max_length=100)

    def __unicode__(self):
        return "Homepage Settings"

    class Meta:
        verbose_name = "Homepage Settings"
        verbose_name_plural = "Homepage Settings"


class FAQPageSettings(models.Model):
    heading = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return "FAQ Page Settings"

    class Meta:
        verbose_name = "FAQ Page Settings"
        verbose_name_plural = "FAQ Page Settings"
