# Generated by Django 2.2.3 on 2020-06-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('PatientName', models.CharField(max_length=30)),
                ('PatientDOB', models.DateField(max_length=20, null=True)),
                ('PatientID', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
