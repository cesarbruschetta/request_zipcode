# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('request_zipcode.zipcode.views',

                       url(r'^crossdomain.xml$',
                           'crossdomain', name='crossdomain'),

                       url(r'^cep/(?P<cep>\d{5}-?\d{3})/?$',
                           'cep_check', name='cep_check'),
                       )
