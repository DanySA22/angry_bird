# Generated by Django 4.2.7 on 2023-12-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_alter_customer_dificulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dificulty',
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='AngryBird24$', max_length=30),
        ),
        migrations.DeleteModel(
            name='Dificulty',
        ),
    ]
