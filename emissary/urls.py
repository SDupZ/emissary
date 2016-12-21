from django.conf.urls import url
from django.contrib import admin

from default.views import home, blog, faq, contact
from delivery.views import create_trip, request_delivery

from django.conf import settings
from django.views.static import serve

from filer.models import Folder, ThumbnailOption

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^blog/$', blog, name='blog'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^contact/$', contact, name='contact'),


    url(r'^create-trip/$', create_trip, name='create_trip'),
    url(r'^request-delivery/$', request_delivery, name='request_delivery'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]


admin.site.unregister(Folder)
admin.site.unregister(ThumbnailOption)
