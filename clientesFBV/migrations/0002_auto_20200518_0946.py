# Generated by Django 2.0.1 on 2020-05-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientesFBV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
