# Generated by Django 3.0.8 on 2020-07-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_auto_20200722_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='photo',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
