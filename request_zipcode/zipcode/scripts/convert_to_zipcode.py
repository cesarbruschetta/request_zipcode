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
        name_model = items.model.__name__
        logger.info('Processando os dados de %s' % (name_model))
        for item in items:
            data = item.to_dict()
            if not ZipCode.objects.filter(cep=data['cep']).exists():
                try:
                    ZipCode.objects.create(**data)
                    logger.info('%s: Cep %(cep)s adcionado com sucesso' % (data,
                                                                           name_model))
                except Exception, ex:
                    logger.error('%s: Error: %s - data: %s' % (str(ex),
                                                               data,
                                                               name_model))
            else:
                logger.info('%s: Cep %(cep)s ja existe no banco de dados' %
                            (data, name_model))

    # PROCESSA LOGRADOUROS (RUAS, AV., ETC.)
    _processor(LogLogradouro.objects.all())
    # PROCESSA LOCALIDADES (CIDADES)
    _processor(LogLocalidade.objects.all())
    # PROCESSA UNIDADES DOS CORREIOS
    _processor(LogUnidOper.objects.all())
    # PROCESSA GRANDES uSUARIOS (EMPRESAS, GOVERNOS, FACULDADES, ETC.)
    _processor(LogGrandeUsuario.objects.all())
