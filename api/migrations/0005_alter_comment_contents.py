# Generated by Django 4.0.5 on 2022-06-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contents',
            field=models.CharField(max_length=1000),
        ),
    ]