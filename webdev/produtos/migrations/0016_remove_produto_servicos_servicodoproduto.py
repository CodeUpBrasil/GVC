# Generated by Django 4.0.2 on 2022-03-12 20:33

from django.db import migrations, models
import django.db.models.deletion

def transfer_product_service_details(apps, schema_editor):
    ServicoDoProduto = apps.get_model('produtos', 'ServicoDoProduto')
    Produto = apps.get_model('produtos', 'Produto')
    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('''
        SELECT prod_serv.produto_id, servicos.nome, servicos.valor
        FROM produtos_produto_servicos as prod_serv
        INNER JOIN fornecedores_servico as servicos ON prod_serv.servico_id=servicos.id
    ''')
    servicos = cursor.fetchall()
    
    for servico in servicos:
        ServicoDoProduto.objects.create(
            produto=Produto.objects.get(pk=servico[0]),
            nome=servico[1],
            valor=servico[2],
        )

class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0015_alter_produto_data_criacao'),
    ]

    
    operations = [
        migrations.CreateModel(
            name='ServicoDoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto', verbose_name='produto')),
            ],
        ),
        migrations.RunPython(transfer_product_service_details),
    ]