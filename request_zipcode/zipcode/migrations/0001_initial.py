# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [

        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cep', models.CharField(default=b'', max_length=16L, db_index=True)),
                ('logradouro', models.CharField(default=b'', max_length=125L)),
                ('bairro', models.CharField(default=b'', max_length=72L)),
                ('cidade', models.CharField(default=b'', max_length=60L, blank=True)),
                ('estado', models.CharField(default=b'', max_length=72L)),
                ('estado_sigla', models.CharField(default=b'', max_length=2L)),
            ],
        ),
    ]
