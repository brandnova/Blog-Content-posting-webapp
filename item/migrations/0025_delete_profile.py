# Generated by Django 4.2.7 on 2023-12-13 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0024_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]