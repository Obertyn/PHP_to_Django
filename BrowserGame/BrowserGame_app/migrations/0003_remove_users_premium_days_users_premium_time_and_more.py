# Generated by Django 4.1.2 on 2022-11-20 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrowserGame_app', '0002_users_food_users_premium_days_users_stone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='premium_days',
        ),
        migrations.AddField(
            model_name='users',
            name='premium_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 13, 13, 30, 688087)),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=130),
        ),
    ]