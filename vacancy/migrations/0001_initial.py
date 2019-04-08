# Generated by Django 2.1.5 on 2019-03-31 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('passport_no', models.CharField(max_length=10)),
                ('DOB', models.DateField()),
                ('DOI', models.DateField()),
                ('DOE', models.DateField()),
                ('father_name', models.CharField(max_length=100)),
                ('Marital_Status', models.IntegerField()),
                ('Citizenship', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('perm_address', models.CharField(max_length=100)),
                ('Ref', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=20)),
                ('clientimage', models.ImageField(null=True, upload_to='Client/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('qualifications', models.CharField(max_length=500)),
                ('fooding', models.IntegerField(default=0)),
                ('lodging', models.IntegerField(default=0)),
                ('insurance', models.IntegerField(default=0)),
                ('listed_date', models.DateField(auto_now=True)),
                ('last_date', models.DateField()),
                ('time_period', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to='Vacancies/Image/%Y/%m/%d')),
                ('companyjobs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='vacancy.Company')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='appliedjob',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applied', to='vacancy.Jobs'),
        ),
    ]