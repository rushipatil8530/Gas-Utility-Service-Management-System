# Generated by Django 3.2.8 on 2024-04-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsApp', '0002_auto_20240424_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '1. Total Customers'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '2. Total Orders'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]