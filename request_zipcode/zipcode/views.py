# -*- coding: utf-8 -*-

from django.http import HttpResponse

from request_zipcode.zipcode.utils import cep_find

import simplejson as json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def cep_check(request, cep):
    cep = cep.replace('-', '')
    try:
        data = cep_find(cep)
        data['success'] = True

        # ATERAÇÂO PARA A COMPATIBILIDADE COM OUTRAS API
        # data.update({'localidade': data.get('cidade', ''),
        #              'uf': data.get('estado', '')})

    except Exception, ex:
        logger.error('Erro no cep: %s' % (str(ex)))
        data = {}

    return HttpResponse(json.dumps(data), content_type='application/json')


def crossdomain(request):
    html = '''
        <?xml version="1.0"?>
        <cross-domain-policy>
            <allow-access-from domain="*"/>
        </cross-domain-policy>
    '''
    return HttpResponse(html)
