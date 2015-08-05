# coding: utf-8

from request_zipcode.zipcode.models import (LogLogradouro, LogLocalidade,
                                            LogUnidOper, LogGrandeUsuario,
                                            ZipCode)


import logging
logger = logging.getLogger(__name__)


def run(*args):
    '''
        Script utilizado para migrar o cep da base dos seguimentada,
        para uma base simples com apenas os dados nesseçarios para o
        cadastro de usuarios em um ecommecer ou outras aplicações.

    '''
    def _processor(items):
        logger.info('Processando os dados de %s' % (items.model.__name__))
        for item in items:
            data = item.to_dict()
            if not ZipCode.objects.filter(cep=data['cep']).exists():
                ZipCode.objects.create(**data)
            else:
                logger.info('Cep %(cep)s ja existe no banco de dados' % (data))

    _processor(LogLogradouro.objects.all())
    _processor(LogLocalidade.objects.all())
    _processor(LogUnidOper.objects.all())
    _processor(LogGrandeUsuario.objects.all())
    # print LogLogradouro.objects.all().count()
    # print LogLocalidade.objects.all().count()
    # print LogUnidOper.objects.all().count()
    # print LogGrandeUsuario.objects.all().count()
