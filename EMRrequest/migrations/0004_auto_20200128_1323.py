# Generated by Django 2.2.5 on 2020-01-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMRrequest', '0003_auto_20200128_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emrrequest',
            name='Status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
