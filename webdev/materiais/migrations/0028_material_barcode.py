# Generated by Django 4.0.4 on 2022-05-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0027_alter_material_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to='materiais/barcode/', verbose_name='código de barras'),
        ),
    ]