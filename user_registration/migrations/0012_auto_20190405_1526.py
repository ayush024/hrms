# Generated by Django 2.2 on 2019-04-05 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0011_auto_20190405_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2019, 4, 5, 15, 26, 0, 515493)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2019, 4, 5, 15, 26, 0, 515285)),
        ),
    ]
