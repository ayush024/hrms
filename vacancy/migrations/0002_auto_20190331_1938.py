# Generated by Django 2.1.5 on 2019-03-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='clientimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
