# Generated by Django 5.1.4 on 2024-12-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_alter_reserva_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.CharField(max_length=100),
        ),
    ]
