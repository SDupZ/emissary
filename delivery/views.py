from django.shortcuts import render


def create_trip(request):
    template = 'create-trip.html'
    context = {}
    return render(request, template, context)


def request_delivery(request):
    template = 'request-delivery.html'
    context = {}
    return render(request, template, context)
