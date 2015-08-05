# -*- coding: utf-8 -*-

from django.db import models


class LogFaixaBairro(models.Model):
    bai_nu_sequencial = models.ForeignKey('zipcode.LogBairro',
                                          db_column='bai_nu_sequencial')
    fcb_nu_ordem = models.IntegerField()
    fcb_rad_ini = models.CharField(max_length=5L)
    fcb_suf_ini = models.CharField(max_length=3L)
    fcb_rad_fim = models.CharField(max_length=5L)
    fcb_suf_fim = models.CharField(max_length=3L)

    class Meta:
        db_table = 'log_faixa_bairro'
        app_label = 'zipcode'
        managed = False
