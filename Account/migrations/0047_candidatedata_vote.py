# Generated by Django 3.0.8 on 2020-07-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0046_candidatedata_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatedata',
            name='Vote',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
