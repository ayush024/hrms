# Generated by Django 2.2 on 2019-04-04 05:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0005_auto_20190402_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='endDate',
            field=models.DateField(default=datetime.date(2019, 4, 4)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startDate',
            field=models.DateField(default=datetime.date(2019, 4, 4)),
        ),
    ]