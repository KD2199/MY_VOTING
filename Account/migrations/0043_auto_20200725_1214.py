# Generated by Django 3.0.8 on 2020-07-25 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0042_auto_20200725_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatedata',
            old_name='PartName',
            new_name='PartyName',
        ),
    ]
