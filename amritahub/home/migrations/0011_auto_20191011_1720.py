# Generated by Django 2.1.5 on 2019-10-11 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191011_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='home/static/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]
