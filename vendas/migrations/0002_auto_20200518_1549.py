# Generated by Django 2.0.1 on 2020-05-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='venda',
            name='impostos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vendaproduto',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
