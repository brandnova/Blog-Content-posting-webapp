# Generated by Django 4.2.7 on 2023-12-29 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_uservisit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservisit',
            name='date',
        ),
    ]
