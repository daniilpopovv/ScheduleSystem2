# Generated by Django 4.0.4 on 2022-06-19 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScheduleSystem', '0004_alter_students_id_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='views',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_attendance',
            field=models.DateField(verbose_name='Дата посещаемости'),
        ),
    ]
