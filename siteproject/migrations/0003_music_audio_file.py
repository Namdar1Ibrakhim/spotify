# Generated by Django 4.1.7 on 2023-04-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteproject', '0002_adminuser_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
