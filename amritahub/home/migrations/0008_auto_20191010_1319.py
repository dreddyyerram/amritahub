# Generated by Django 2.1.5 on 2019-10-10 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191010_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]
