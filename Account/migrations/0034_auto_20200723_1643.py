# Generated by Django 3.0.8 on 2020-07-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0033_auto_20200723_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Profile_Photo',
            field=models.FileField(upload_to='images'),
        ),
    ]
