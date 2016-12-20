from django.conf.urls import url
from django.contrib import admin

from default.views import home, blog, faq, contact

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^blog/$', blog, name='blog'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^contact/$', contact, name='contact'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]
