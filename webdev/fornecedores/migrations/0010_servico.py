# Generated by Django 3.1.5 on 2021-05-04 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0009_auto_20210503_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Serviço')),
                ('data', models.DateField(default=datetime.date(2021, 5, 4), verbose_name='Data')),
                ('qualidade', models.IntegerField(default=0, verbose_name='Qualidade')),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total Pago')),
                ('fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fornecedores.fornecedor', verbose_name='Fornecedor')),
            ],
        ),
    ]
