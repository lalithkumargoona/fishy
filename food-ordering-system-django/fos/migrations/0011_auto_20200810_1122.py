# Generated by Django 3.0.8 on 2020-08-10 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fos', '0010_auto_20200810_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddetails',
            old_name='discription',
            new_name='description',
        ),
    ]