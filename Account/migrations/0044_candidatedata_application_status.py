# Generated by Django 3.0.8 on 2020-07-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0043_auto_20200725_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatedata',
            name='Application_Status',
            field=models.BooleanField(default=False),
        ),
    ]