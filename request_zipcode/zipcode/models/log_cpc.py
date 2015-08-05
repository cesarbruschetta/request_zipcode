# -*- coding: utf-8 -*-

from django.db import models


class LogCpc(models.Model):

    cpc_nu_sequencial = models.IntegerField(primary_key=True)
    ufe_sg = models.CharField(max_length=2L)
    loc_nu_sequencial = models.ForeignKey('LogLocalidade',
                                          db_column='loc_nu_sequencial')
    cep = models.CharField(max_length=16L)
    cpc_no = models.CharField(max_length=96L)
    cpc_endereco = models.CharField(max_length=108L)
    cpc_tipo = models.CharField(max_length=2L, blank=True)
    cpc_abrangencia = models.CharField(max_length=80L, blank=True)
    temp = models.CharField(max_length=8L, blank=True)

    class Meta:
        db_table = 'log_cpc'
        app_label = 'zipcode'
        managed = False
