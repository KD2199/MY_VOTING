# Generated by Django 3.0.8 on 2020-07-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EVM', '0003_auto_20200715_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggedinuser',
            name='session_key',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]