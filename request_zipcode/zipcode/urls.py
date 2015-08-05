# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('zipcode.views',

                       url(r'^crossdomain.xml$',
                           'crossdomain', name='crossdomain'),
                       url(r'^ /cep/(?P<cep>\d{5}-?\d{3})/?$',
                           'find_cep', name='find_cep'),
                       )
