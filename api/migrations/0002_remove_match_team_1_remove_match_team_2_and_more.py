# Generated by Django 4.0.3 on 2022-03-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team_1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='match',
            name='team_1_name',
            field=models.CharField(default='asdasd', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='team_2_name',
            field=models.CharField(default='asdasd', max_length=200),
            preserve_default=False,
        ),
    ]
