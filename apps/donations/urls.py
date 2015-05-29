from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # url(r'^$', 'apps.donations.views.list', name='list'),
    # url(r'^(?P<blood_id>[0-9]+)/$', 'apps.donations.views.blood',
    #     name='blood'),
    # url(r'^(?P<blood_id>[0-9]+)/hospital-tests/$',
    #     'apps.donations.views.hospital', name='hospital'),
    # url(r'^(?P<blood_id>[0-9]+)/nbts-tests/$',
    #     'apps.donations.views.nbts', name='nbts'),
    # url(r'^(?P<blood_id>[0-9]+)/donor/$',
    #     'apps.donations.views.donor', name='donor'),

    # url(r'^donors/$', 'apps.donations.views.donors', name='donors'),

    url(r'^donors/donate/$', 'apps.donations.views.donate_details',
        name='donate_details'),
    url(r'^donors/donate/(?P<donor_id>[0-9]+)/pre-form$',
        'apps.donations.views.donate_pre_form', name='donate_pre_form'),
    url(r'^donors/donate/(?P<donor_id>[0-9]+)/formA$',
        'apps.donations.views.donate_form_a', name='donate_form_a'),
    url(r'^donors/donate/(?P<donor_id>[0-9]+)/formB$',
        'apps.donations.views.donate_form_b', name='donate_form_b'),
    url(r'^donors/donate/(?P<donor_id>[0-9]+)/formC$',
        'apps.donations.views.donate_form_c', name='donate_form_c'),

    # url(r'^donors/(?P<donor_id>[0-9]+)/$', 'apps.donations.views.donor',
    #     name='donor'),
    # url(r'^donors/(?P<donor_id>[0-9]+)/$', 'apps.donations.views.donor',
    #     name='donor'),
)
