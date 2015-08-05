# -*- coding: utf-8 -*-
from django.core.cache import get_cache

from pingo.utils.CepTracker import CepTracker
from zipcode.models import (LogLogradouro, LogLocalidade,
                            LogUnidOper, LogGrandeUsuario)

import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


def _processor(cep):
    try:
        # BUSCA O CEP NA BASE NORMAL (DADOS COMPLETOS)
        result = LogLogradouro.objects.get(cep=cep)
        return result.to_dict()
    except LogLogradouro.DoesNotExist:
        try:
            # BUSCA O CEP NA BASE DE CEP DA CIDADE (DADOS INCOMPLETOS)
            result = LogLocalidade.objects.get(cep=cep)
            return result.to_dict()
        except LogLocalidade.DoesNotExist:
            try:
                # BUSCA O CEP NA BASE DE CAIXAS POSTAIS (DADOS COMPLETOS)
                result = LogUnidOper.objects.get(cep=cep)
                return result.to_dict()
            except LogUnidOper.DoesNotExist:
                try:
                    # BUSCA O CEP NA BASE DE GRANDES USUARIOS (DADOS COMPLETOS)
                    result = LogGrandeUsuario.objects.get(cep=cep)
                    return result.to_dict()
                except LogGrandeUsuario.DoesNotExist:
                    # NAO ACHOU O CEP
                    # BUSCA NO WEBSERVE DOS CORREIOS

                    # Lib do POSTMON
                    # postmon.com.br/
                    result = CepTracker().track(cep)

                    if len(result):
                        return result[0]
                    else:
                        logger.info('CEP inesistente : %s' % (cep))
                        return {}


def cep_find(cep):
    cache = get_cache('default')
    key = 'zipcode:{0}'.format(cep)

    cached_data = cache.get(key)
    if cached_data:
        return cached_data

    data = _processor(cep)
    if data:
        timeout = 60 * 60 * 24 * 30
        cache.set(key, data, timeout)

    return data
