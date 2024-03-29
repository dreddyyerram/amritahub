# Generated by Django 2.1.5 on 2019-11-05 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191016_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='campus',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
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
            model_name='friendrequest',
            name='From_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='requested_user_profile', serialize=False, to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='To_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user_profile', to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='admin',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]
