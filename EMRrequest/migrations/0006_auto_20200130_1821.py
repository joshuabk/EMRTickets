# Generated by Django 2.2.5 on 2020-01-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMRrequest', '0005_emrrequest_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emrrequest',
            name='Comment',
            field=models.CharField(default='', max_length=300),
        ),
    ]