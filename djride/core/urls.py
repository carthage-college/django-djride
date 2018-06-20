from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView

from django.contrib import admin

admin.autodiscover()

handler404 = 'djtools.views.errors.four_oh_four_error'
handler500 = 'djtools.views.errors.server_error'


urlpatterns = [
    url(
        r'^admin/', include(admin.site.urls)
    ),
    # shuttle tracker
    url(
        r'^shuttle/', include('djride.shuttle.urls')
    ),
]
