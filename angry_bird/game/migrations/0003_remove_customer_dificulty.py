# Generated by Django 4.2.7 on 2023-11-17 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_customer_dificulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dificulty',
        ),
    ]
