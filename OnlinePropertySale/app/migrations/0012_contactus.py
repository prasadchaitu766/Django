# Generated by Django 2.1.7 on 2019-02-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190214_0544'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
