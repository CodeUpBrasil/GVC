# Generated by Django 4.0.2 on 2022-03-12 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0015_alter_produto_data_criacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='servicos',
        ),
        migrations.CreateModel(
            name='ServicoDoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='serviço')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='total pago')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto', verbose_name='produto')),
            ],
        ),
    ]
