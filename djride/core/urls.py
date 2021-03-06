from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView, TemplateView

from django.contrib.auth import views as auth_views

from django.contrib import admin

admin.autodiscover()

handler404 = 'djtools.views.errors.four_oh_four_error'
handler500 = 'djtools.views.errors.server_error'


urlpatterns = [
    # auth
    url(
        r'^accounts/login/$', auth_views.login,
        {'template_name': 'accounts/login.html'},
        name='auth_login'
    ),
    url(
        r'^accounts/logout/$', auth_views.logout,
        {'next_page': reverse_lazy('auth_loggedout')},
        name='auth_logout'
    ),
    url(
        r'^accounts/loggedout/$', loggedout,
        {'template_name': 'accounts/logged_out.html'},
        name='auth_loggedout'
    ),
    url(
        r'^accounts/profile/sender/manager/$', sender_manager,
        name='sender_manager'
    ),
    url(
        r'^accounts/profile/sender/manager/(?P<sid>\w+)/(?P<action>[-\w]+)/$',
        sender_manager, name='sender_update'
    ),
    url(
        r'^accounts/profile/$', user_profile,
        name='user_profile'
    ),
    url(
        r'^accounts/$',
        RedirectView.as_view(url=reverse_lazy('auth_login'))
    ),
    url(
        r'^denied/$',
        TemplateView.as_view(
            template_name='denied.html'
        ), name='access_denied'
    ),
    # django admin
    url(
        r'^admin/', include(admin.site.urls)
    ),
    # shuttle tracker
    url(
        r'^shuttle/', include('djride.shuttle.urls')
    ),
]
