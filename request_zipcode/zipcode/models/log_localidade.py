# -*- coding: utf-8 -*-

from django.db import models


class LogLocalidade(models.Model):

    class Meta:
        db_table = 'log_localidade'
        app_label = 'zipcode'
        managed = False

    loc_nu_sequencial = models.IntegerField(primary_key=True)
    loc_nosub = models.CharField(max_length=50L, blank=True)
    loc_no = models.CharField(max_length=60L, blank=True)
    cep = models.CharField(max_length=16L, blank=True)
    ufe_sg = models.ForeignKey('zipcode.LogFaixaUf', null=True,
                               db_column='ufe_sg', blank=True)
    loc_in_situacao = models.IntegerField(null=True, blank=True)
    loc_in_tipo_localidade = models.CharField(max_length=1L)
    loc_nu_sequencial_sub = models.IntegerField(null=True, blank=True)
    temp = models.CharField(max_length=8L, blank=True)

    @property
    def uf_name(self):
        return self.ufe_sg.ufe_no

    @property
    def uf_sigla(self):
        return self.ufe_sg.ufe_sg

    def to_dict(self):
        return {
            'logradouro': '', 'bairro': '',
            'cidade': self.loc_no,
            'estado': self.uf_name,
            'estado_sigla': self.uf_sigla,
            'cep': self.cep
        }
