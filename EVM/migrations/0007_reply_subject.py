# Generated by Django 3.0.8 on 2020-07-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EVM', '0006_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='Subject',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]