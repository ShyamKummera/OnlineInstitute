# Generated by Django 2.2.12 on 2020-07-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleNewClass',
            fields=[
                ('course_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=60)),
                ('faculty', models.CharField(max_length=60)),
                ('date_course_start', models.DateField()),
                ('time_start', models.TimeField()),
                ('fee', models.FloatField()),
                ('duration', models.IntegerField(max_length=60)),
            ],
        ),
    ]
