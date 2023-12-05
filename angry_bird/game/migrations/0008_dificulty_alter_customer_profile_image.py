# Generated by Django 4.2.7 on 2023-12-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_customer_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dificulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=300, upload_to=''),
        ),
    ]
