# Generated by Django 3.2.7 on 2021-10-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0025_auto_20210705_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
