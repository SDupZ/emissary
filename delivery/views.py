from django.shortcuts import render
from default.forms import ContactForm
from delivery.forms import TripForm


def create_trip(request):
    template = 'create-trip.html'
    form_class = TripForm
    context = {}

    if request.method == 'POST':

        form = form_class(data=request.POST)
        import pdb; pdb.set_trace()
        if form.is_valid():
            template = 'create-trip-complete.html'
            form.save()


    return render(request, template, context)


def request_delivery(request):
    template = 'request-delivery.html'
    context = {}
    return render(request, template, context)
