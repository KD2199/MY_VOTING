# Generated by Django 3.0.8 on 2020-07-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0015_auto_20200722_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='photo',
            field=models.ImageField(blank=True, default='user.jpg', null=True, upload_to=''),
        ),
    ]
