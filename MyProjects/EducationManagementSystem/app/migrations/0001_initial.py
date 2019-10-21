# Generated by Django 2.1.4 on 2018-12-17 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='campuses',
            fields=[
                ('campus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('campusname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='front_office_module',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('joining_date', models.DateField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cities', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('material_status', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='transfer_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='campuses',
            name='cityname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city'),
        ),
    ]