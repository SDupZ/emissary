from django.forms import ModelForm
from delivery.models import Trip


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = [
            'origin_street_number',
            'origin_street_name',
            'origin_city',
            'origin_country',
            'origin_post_code',
            'destination_street_number',
            'destination_street_name',
            'destination_city',
            'destination_country',
            'destination_post_code',
            'date',
            'leaving_time',
        ]
