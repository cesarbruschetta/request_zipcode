# -*- coding: utf-8 -*-

from django.db import models


class LogFaixaUf(models.Model):

    ufe_sg = models.CharField(max_length=2L, primary_key=True)
    ufe_no = models.CharField(max_length=72L)
    ufe_rad1_ini = models.CharField(max_length=5L)
    ufe_suf1_ini = models.CharField(max_length=3L)
    ufe_rad1_fim = models.CharField(max_length=5L)
    ufe_suf1_fim = models.CharField(max_length=3L)
    ufe_rad2_ini = models.CharField(max_length=5L, blank=True)
    ufe_suf2_ini = models.CharField(max_length=3L, blank=True)
    ufe_rad2_fim = models.CharField(max_length=5L, blank=True)
    ufe_suf2_fim = models.CharField(max_length=3L, blank=True)

    class Meta:
        db_table = 'log_faixa_uf'
        app_label = 'zipcode'
        managed = False
