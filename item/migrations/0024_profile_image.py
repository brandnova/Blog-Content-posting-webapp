# Generated by Django 4.2.7 on 2023-12-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0023_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images'),
        ),
    ]