# Generated by Django 3.0.8 on 2020-07-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0038_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Profile_Image', models.ImageField(null=True, upload_to='Profile_Image')),
            ],
        ),
    ]