# Generated by Django 4.2.7 on 2023-12-04 09:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0022_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, null=True),
        ),
    ]