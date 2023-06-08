# Generated by Django 4.1.7 on 2023-04-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cliente_options_alter_fabricante_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabelaPreco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
            ],
            options={
                'verbose_name_plural': 'TabelaPrecos',
            },
        ),
    ]
