# -*- coding: utf-8 -*-

from django.db import models


from .log_bairro import LogBairro
from .log_cpc import LogCpc
from .log_faixa_bairro import LogFaixaBairro
from .log_faixa_localidade import LogFaixaLocalidade
from .log_faixa_uf import LogFaixaUf
from .log_faixa_uop import LogFaixaUop
from .log_grande_usuario import LogGrandeUsuario
from .log_localidade import LogLocalidade
from .log_logradouro import LogLogradouro
from .log_unid_oper import LogUnidOper
from .zipcode import ZipCode


class LogFaixaCpc(models.Model):
    cpc_nu_sequencial = models.ForeignKey('zipcode.LogCpc',
                                          db_column='cpc_nu_sequencial')
    cpc_nu_inicial = models.IntegerField()
    cpc_nu_final = models.IntegerField()

    class Meta:
        db_table = 'log_faixa_cpc'
        app_label = 'zipcode'


class LogTipoLogr(models.Model):
    tipologradouro = models.CharField(max_length=10L, blank=True)

    class Meta:
        db_table = 'log_tipo_logr'
        app_label = 'zipcode'
