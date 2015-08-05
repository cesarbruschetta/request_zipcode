# -*- coding: utf-8 -*-

from django.db import models


class ZipCode(models.Model):

    class Meta:
        app_label = 'zipcode'
        verbose_name = 'CEP'
        verbose_name_plural = 'CEPs'

    cep = models.CharField(max_length=16L, db_index=True, default='')
    logradouro = models.CharField(max_length=125L, default='')
    bairro = models.CharField(max_length=72L, default='')
    cidade = models.CharField(max_length=60L, blank=True, default='')
    estado = models.CharField(max_length=72L, default='')
    estado_sigla = models.CharField(max_length=2L, default='')

    def __unicode__(self):
        return 'CEP: %s' % (self.cep)

    def str_admin(self):
        return '%(logradouro)s - %(bairro)s -\
                %(cidade)s, %(estado_sigla)s' % (self.__dict__)
