# Generated by Django 2.1.5 on 2019-04-01 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0003_auto_20190401_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='end_date',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='start_date',
            new_name='startDate',
        ),
    ]