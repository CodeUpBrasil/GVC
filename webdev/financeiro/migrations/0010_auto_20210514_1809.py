# Generated by Django 3.1.5 on 2021-05-14 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0009_auto_20210514_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='parcelas',
            field=models.IntegerField(choices=[(1, '1x'), (2, '2x'), (3, '3x'), (4, '4x'), (5, '5x'), (6, '6x'), (7, '7x'), (8, '8x'), (9, '9x'), (10, '10x'), (11, '11x'), (12, '12x')], default=1, verbose_name='Parcelas'),
        ),
    ]