# Generated by Django 2.1.5 on 2019-10-15 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('home', '0014_auto_20191015_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(default=None, null=True, unique=True)),
                ('date', models.DateTimeField()),
                ('Description', models.TextField(default=None)),
                ('type', models.CharField(choices=[('S', 'Session'), ('B', 'Workshop')], max_length=1)),
                ('public', models.BooleanField(default=True)),
                ('venue', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='friendrequest',
            fields=[
                ('From_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='requested_user_profile', serialize=False, to='home.Profile')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('To_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user_profile', to='home.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='groupmessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Groupprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DP', models.ImageField(blank=True, null=True, upload_to='home/static/images/')),
                ('dob', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
                ('admin', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
                ('groupname', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='friendactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AddField(
            model_name='events',
            name='Owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]
