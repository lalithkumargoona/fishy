# Generated by Django 3.0.8 on 2020-07-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fos', '0007_auto_20200124_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='cust_phone',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
