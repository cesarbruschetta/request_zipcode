# -*- coding: utf-8 -*-

from django.db import models


class LogUnidOper(models.Model):

    class Meta:
        db_table = 'log_unid_oper'
        app_label = 'zipcode'
        managed = False

    uop_nu_sequencial = models.IntegerField(primary_key=True)
    ufe_sg = models.CharField(max_length=2L)
    loc_nu_sequencial = models.ForeignKey('zipcode.LogLocalidade',
                                          db_column='loc_nu_sequencial')
    log_nu_sequencial = models.ForeignKey('zipcode.LogLogradouro',
                                          db_column='log_nu_sequencial',
                                          blank=True, null=True,)
    bai_nu_sequencial = models.ForeignKey('zipcode.LogBairro',
                                          db_column='bai_nu_sequencial')
    uop_no = models.CharField(max_length=100L)
    cep = models.CharField(max_length=16L)
    uop_endereco = models.CharField(max_length=200L)
    uop_in_cp = models.CharField(max_length=1L, blank=True)
    temp = models.CharField(max_length=8L, blank=True)

    def to_dict(self):
        try:
            logradouro = self.log_nu_sequencial.log_nome
        except:
            logradouro = self.uop_no

        return {
            'logradouro': logradouro,
            'bairro': self.bai_nu_sequencial.bai_no,
            'cidade': self.loc_nu_sequencial.loc_no,
            'estado': self.loc_nu_sequencial.uf_name,
            'estado_sigla': self.loc_nu_sequencial.uf_sigla,
            'cep': self.cep
        }
