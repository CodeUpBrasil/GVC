# Generated by Django 3.1.5 on 2021-06-16 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0021_auto_20210530_1434'),
        ('fornecedores', '0019_auto_20210610_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='total_pago',
            new_name='valor',
        ),
        migrations.AddField(
            model_name='servico',
            name='despesa',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='financeiro.despesa', verbose_name='Despesa'),
        ),
    ]
