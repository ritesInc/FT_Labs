# Generated by Django 2.2 on 2020-03-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200329_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='end_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.CharField(max_length=20),
        ),
    ]
