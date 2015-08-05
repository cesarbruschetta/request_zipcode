# -*- coding: utf-8 -*-

from django.db import models


class LogFaixaLocalidade(models.Model):

    loc_nu_sequencial = models.ForeignKey('zipcode.LogLocalidade',
                                          db_column='loc_nu_sequencial',
                                          primary_key=True,)
    loc_rad1_ini = models.CharField(max_length=5L)
    loc_suf1_ini = models.CharField(max_length=3L)
    loc_rad1_fim = models.CharField(max_length=5L)
    loc_suf1_fim = models.CharField(max_length=3L)
    loc_rad2_ini = models.CharField(max_length=5L, blank=True)
    loc_suf2_ini = models.CharField(max_length=3L, blank=True)
    loc_rad2_fim = models.CharField(max_length=5L, blank=True)
    loc_suf2_fim = models.CharField(max_length=3L, blank=True)

    class Meta:
        db_table = 'log_faixa_localidade'
        app_label = 'zipcode'
        managed = False
