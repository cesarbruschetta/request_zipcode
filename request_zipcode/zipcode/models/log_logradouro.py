# -*- coding: utf-8 -*-

from django.db import models


class LogLogradouro(models.Model):

    class Meta:
        db_table = 'log_logradouro'
        app_label = 'zipcode'
        managed = False

    log_nu_sequencial = models.IntegerField(primary_key=True)
    ufe_sg = models.CharField(max_length=2L)
    loc_nu_sequencial = models.ForeignKey('zipcode.LogLocalidade',
                                          db_column='loc_nu_sequencial')
    log_no = models.CharField(max_length=70L)
    log_nome = models.CharField(max_length=125L)
    bai_nu_sequencial_ini = models.ForeignKey('zipcode.LogBairro',
                                              db_column='bai_nu_sequencial_ini')
    bai_nu_sequencial_fim = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length=16L)
    log_complemento = models.CharField(max_length=100L, blank=True)
    log_tipo_logradouro = models.CharField(max_length=72L, blank=True)
    log_status_tipo_log = models.CharField(max_length=1L)
    log_no_sem_acento = models.CharField(max_length=70L)
    ind_uop = models.CharField(max_length=1L, blank=True)
    ind_gru = models.CharField(max_length=1L, blank=True)
    temp = models.CharField(max_length=8L, blank=True)

    def to_dict(self):
        return {
            'logradouro': self.log_nome,
            'bairro': self.bai_nu_sequencial_ini.bai_no,
            'cidade': self.loc_nu_sequencial.loc_no,
            'estado': self.loc_nu_sequencial.uf_name,
            'estado_sigla': self.loc_nu_sequencial.uf_sigla,
            'cep': self.cep
        }
