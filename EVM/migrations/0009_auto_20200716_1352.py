# Generated by Django 3.0.8 on 2020-07-16 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EVM', '0008_auto_20200716_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='Reply',
            new_name='Response',
        ),
    ]
