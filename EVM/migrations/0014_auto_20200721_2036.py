# Generated by Django 3.0.8 on 2020-07-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EVM', '0013_auto_20200721_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]