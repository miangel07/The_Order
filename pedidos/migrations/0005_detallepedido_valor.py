# Generated by Django 5.0.4 on 2024-04-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_remove_detallepedido_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepedido',
            name='valor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
