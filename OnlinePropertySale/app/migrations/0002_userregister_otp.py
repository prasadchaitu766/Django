# Generated by Django 2.1.7 on 2019-02-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='otp',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]