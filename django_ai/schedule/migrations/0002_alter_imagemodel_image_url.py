# Generated by Django 5.1.2 on 2025-01-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
