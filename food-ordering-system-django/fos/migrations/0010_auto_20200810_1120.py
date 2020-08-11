# Generated by Django 3.0.8 on 2020-08-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fos', '0009_fooddetails_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddetails',
            name='gross_weight',
            field=models.CharField(default=1, max_length=1064),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fooddetails',
            name='image',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='fooddetails',
            name='net_weight',
            field=models.CharField(default=1, max_length=1064),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fooddetails',
            name='price',
            field=models.CharField(max_length=1064),
        ),
    ]
