from django.conf.urls import url
from django.contrib import admin

from home.views import front

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', front, name='front'),
]
