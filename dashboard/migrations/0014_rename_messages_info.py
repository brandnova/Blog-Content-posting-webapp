# Generated by Django 4.2.7 on 2024-01-02 10:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0013_alter_messages_options_alter_messages_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Info',
        ),
    ]
