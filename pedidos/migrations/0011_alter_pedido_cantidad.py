# Generated by Django 5.0.4 on 2024-04-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_remove_detallepedido_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cantidad',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
