# Generated by Django 3.0.8 on 2020-07-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_auto_20200722_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]