# -*- coding: utf-8 -*-

from django.db import models


class LogBairro(models.Model):

    bai_nu_sequencial = models.IntegerField(primary_key=True)
    ufe_sg = models.CharField(max_length=2L)
    loc_nu_sequencial = models.ForeignKey('LogLocalidade',
                                          db_column='loc_nu_sequencial')
    bai_no = models.CharField(max_length=72L)
    bai_no_abrev = models.CharField(max_length=36L, blank=True)

    class Meta:
        app_label = 'zipcode'
        db_table = 'log_bairro'
        managed = False
