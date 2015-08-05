# -*- coding: utf-8 -*-

from django.db import models


class LogFaixaUop(models.Model):

    uop_nu_sequencial = models.ForeignKey('LogUnidOper',
                                          db_column='uop_nu_sequencial')
    fnc_nu_inicial = models.IntegerField()
    fnc_nu_final = models.IntegerField(null=True, blank=True)
    fnc_in_tipo = models.CharField(max_length=255L, blank=True)

    class Meta:
        db_table = 'log_faixa_uop'
        app_label = 'zipcode'
        managed = False
