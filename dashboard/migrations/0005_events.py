# Generated by Django 4.2.7 on 2023-12-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images')),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
