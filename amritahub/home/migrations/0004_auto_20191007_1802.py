# Generated by Django 2.1.5 on 2019-10-07 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20190828_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenteduser', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(default=None, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='home/static/images/')),
                ('date', models.DateField(null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('country', models.TextField(default=None, null=True)),
                ('count', models.IntegerField(default=0)),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='currentpost',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Post'),
        ),
    ]
