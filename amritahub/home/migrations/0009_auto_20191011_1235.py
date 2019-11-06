# Generated by Django 2.1.5 on 2019-10-11 07:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20191010_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]