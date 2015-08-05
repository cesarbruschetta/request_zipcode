# coding: utf-8

from django.contrib import admin
from request_zipcode.zipcode.models import ZipCode


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['str_admin', 'cep']
    search_fields = ['cep', 'logradouro', 'bairro']


admin.site.register(ZipCode, ZipCodeAdmin)
