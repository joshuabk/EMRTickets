# Generated by Django 2.2.3 on 2020-07-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyQA', '0002_auto_20200719_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyqa',
            name='QATestDate',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
