from django.conf.urls import url

from djride.shuttle import views

urlpatterns = [
    url(
        r'^$',
        views.map, name='map'
    ),
]
