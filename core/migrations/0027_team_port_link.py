# Generated by Django 4.2.7 on 2024-01-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_terms_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='port_link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
