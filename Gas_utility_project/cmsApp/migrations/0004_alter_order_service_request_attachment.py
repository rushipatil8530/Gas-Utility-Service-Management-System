# Generated by Django 3.2.8 on 2024-04-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsApp', '0003_auto_20240424_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service_request_attachment',
            field=models.FileField(blank=True, null=True, upload_to='upload_to="static/images/'),
        ),
    ]
