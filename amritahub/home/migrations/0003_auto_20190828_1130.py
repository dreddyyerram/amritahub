# Generated by Django 2.1.5 on 2019-08-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190827_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='home/static/images/'),
        ),
    ]
