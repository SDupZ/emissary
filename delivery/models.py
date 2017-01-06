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

    origin_street_number = models.CharField(blank=True, null=True, max_length=10)
    origin_street_name = models.CharField(blank=True, null=True, max_length=100)
    origin_city = models.CharField(blank=True, null=True, max_length=50)
    origin_country = models.CharField(blank=True, null=True, max_length=40)
    origin_post_code = models.CharField(blank=True, null=True, max_length=5)

    destination_street_number = models.CharField(blank=True, null=True, max_length=10)
    destination_street_name = models.CharField(blank=True, null=True, max_length=100)
    destination_city = models.CharField(blank=True, null=True, max_length=50)
    destination_country = models.CharField(blank=True, null=True, max_length=40)
    destination_post_code = models.CharField(blank=True, null=True, max_length=5)

    date = models.CharField(blank=True, null=True, max_length=20)
    leaving_time = models.CharField(blank=True, null=True, max_length=5)

    def __unicode__(self):
        return "Trip id " + self.pk

    class Meta:
        verbose_name = "Trip"
