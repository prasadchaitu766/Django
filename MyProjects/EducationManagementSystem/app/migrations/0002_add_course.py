# Generated by Django 2.1.4 on 2018-12-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=20)),
                ('Duration', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
