# Generated by Django 2.2 on 2019-04-06 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0013_auto_20190406_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='netsalary',
            name='given',
        ),
        migrations.AlterField(
            model_name='leave',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 4, 6, 12, 6, 37, 243716)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 4, 6, 12, 6, 37, 243507)),
        ),
    ]