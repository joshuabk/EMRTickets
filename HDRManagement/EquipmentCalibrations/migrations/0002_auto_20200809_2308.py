# Generated by Django 2.2.3 on 2020-08-09 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EquipmentCalibrations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveymeter',
            old_name='CalibraionDate',
            new_name='CalibrationDate',
        ),
        migrations.RenameField(
            model_name='surveymeter',
            old_name='CalibraionDue',
            new_name='CalibrationDue',
        ),
    ]