# Generated by Django 2.2 on 2019-04-05 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0007_user_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='endDate',
            field=models.DateField(default=datetime.date(2019, 4, 5)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startDate',
            field=models.DateField(default=datetime.date(2019, 4, 5)),
        ),
    ]
