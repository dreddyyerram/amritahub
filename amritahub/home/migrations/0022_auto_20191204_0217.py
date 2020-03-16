# Generated by Django 2.1.5 on 2019-12-03 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20191202_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
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
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='requested_user_profile', to='home.Profile'),
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