# Generated by Django 2.2.5 on 2020-02-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMRrequest', '0011_auto_20200220_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emrrequest',
            name='DateCompleted',
            field=models.DateTimeField(null=True),
        ),
    ]
