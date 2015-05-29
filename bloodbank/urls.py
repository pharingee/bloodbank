from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'apps.common.views.home', name='home'),
    url(r'^login/$', 'apps.common.views.user_login', name='login'),
    url(r'^logout/$', 'apps.common.views.user_logout', name='logout'),
    url(r'^dashboard/$', 'apps.common.views.dashboard', name='dashboard'),
    url(r'^users/', include('apps.users.urls', namespace='users')),
    url(r'^donations/', include('apps.donations.urls', namespace='donations')),
    url(r'^transfusions/', include('apps.transfusions.urls',
        namespace='transfusions')),

    url(r'^admin/', include(admin.site.urls)),
)
