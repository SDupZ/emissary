from datetime import datetime
from django.db import models

# class DeliveryRequest(models.Model):
#     created = models.DateTimeField(db_index=True, auto_now_add=True)
#     modified = models.DateTimeField(db_index=True, auto_now=True)
#
#     question = models.CharField(blank=True, null=True, max_length=100)
#     answer = RichTextField(blank=True, null=True)
#
#     def __unicode__(self):
#         return self.question
#
#     class Meta:
#         verbose_name = "FAQ Item"


class Trip(models.Model):
    # created = models.DateTimeField(db_index=True, auto_now_add=True)
    # modified = models.DateTimeField(db_index=True, auto_now=True)

    origin_street_number = models.CharField(blank=True, null=True, max_length=100)
    origin_street_name = models.CharField(blank=True, null=True, max_length=1000)
    origin_city = models.CharField(blank=True, null=True, max_length=500)
    origin_country = models.CharField(blank=True, null=True, max_length=400)
    origin_post_code = models.CharField(blank=True, null=True, max_length=50)

    destination_street_number = models.CharField(blank=True, null=True, max_length=100)
    destination_street_name = models.CharField(blank=True, null=True, max_length=1000)
    destination_city = models.CharField(blank=True, null=True, max_length=500)
    destination_country = models.CharField(blank=True, null=True, max_length=400)
    destination_post_code = models.CharField(blank=True, null=True, max_length=50)

    date = models.CharField(blank=True, null=True, max_length=200)
    leaving_time = models.CharField(blank=True, null=True, max_length=50)

    def __unicode__(self):
        return "Trip id " + self.pk

    class Meta:
        verbose_name = "Trip"
