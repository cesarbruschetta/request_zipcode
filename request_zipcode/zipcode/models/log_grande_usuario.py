# -*- coding: utf-8 -*-

from django.db import models


class LogGrandeUsuario(models.Model):

    class Meta:
        db_table = 'log_grande_usuario'
        app_label = 'zipcode'
        managed = False

    gru_nu_sequencial = models.IntegerField(primary_key=True)
    ufe_sg = models.CharField(max_length=2L)
    loc_nu_sequencial = models.ForeignKey('LogLocalidade',
                                          db_column='loc_nu_sequencial')
    log_nu_sequencial = models.ForeignKey('LogLogradouro',
                                          db_column='log_nu_sequencial',
                                          blank=True, null=True)
    bai_nu_sequencial = models.ForeignKey('zipcode.LogBairro',
                                          db_column='bai_nu_sequencial')
    gru_no = models.CharField(max_length=96L)
    cep = models.CharField(max_length=16L)
    gru_endereco = models.CharField(max_length=200L)
    temp = models.CharField(max_length=8L, blank=True)

    def to_dict(self):
        return {
            'logradouro': self.log_nu_sequencial.log_nome,
            'bairro': self.bai_nu_sequencial.bai_no,
            'cidade': self.loc_nu_sequencial.loc_no,
            'estado': self.loc_nu_sequencial.uf_name,
            'estado_sigla': self.loc_nu_sequencial.uf_sigla,
            'cep': self.cep
        }
