# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosisinfo',
            name='So_Throat',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Sor_Throat',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=128, null=True),
        ),
    ]
