# Generated by Django 2.2.3 on 2020-08-02 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceExchangeQA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SourceCertificate', models.FileField(default='no File', upload_to='')),
                ('QADate', models.DateTimeField(null=True)),
                ('DoorTest', models.BooleanField(default=True)),
                ('EmergencyStopTest', models.BooleanField(default=True)),
                ('PrimeAlertTest', models.BooleanField(default=True)),
                ('IndexerInterlockTest', models.BooleanField(default=True)),
                ('ApplicatorNotInsertedTest', models.BooleanField(default=True)),
                ('PauseTest', models.BooleanField(default=True)),
                ('Completed', models.BooleanField(default=True)),
                ('StatedKerma', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('MeasuredKerma', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('SourceActivity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('CalculatedActivity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('SourcePositionMeasured', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('SourcePositionProgramed', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('SurveyMeter', models.CharField(max_length=30, null=True)),
                ('SurveyMCalibrationDue', models.DateTimeField(null=True)),
                ('Temperature', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Pressure', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('WellChamber', models.CharField(max_length=30, null=True)),
                ('WellChamberCalDue', models.DateTimeField(null=True)),
                ('WellChamberCalFactor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Electrometer', models.CharField(max_length=30, null=True)),
                ('ElectrometerCalDue', models.DateTimeField(null=True)),
                ('ElectrometerCalFactor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TimerLinearity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seconds15', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Seconds30', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Seconds45', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Seconds60', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('SourceExchangeQA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SourceExchange.SourceExchangeQA')),
            ],
        ),
        migrations.CreateModel(
            name='SweetSpotMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SourceExchangeQA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SourceExchange.SourceExchangeQA')),
            ],
        ),
    ]
