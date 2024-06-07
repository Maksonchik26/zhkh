# Generated by Django 5.0.6 on 2024-06-07 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=256, unique=True)),
                ('progress', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='Pending', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('WATER', 'Water'), ('MAINTENANCE', 'Maintenance')], max_length=128)),
                ('unit_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FlatRentCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_rent', models.FloatField()),
                ('maintenance_rent', models.FloatField()),
                ('total_rent', models.FloatField()),
                ('month', models.CharField(max_length=7)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_rent_calculations', to='zhkh.flat')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='zhkh.house'),
        ),
        migrations.CreateModel(
            name='WaterMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_meters', to='zhkh.flat')),
            ],
            options={
                'unique_together': {('flat', 'name')},
            },
        ),
        migrations.CreateModel(
            name='WaterMeterReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reading', models.FloatField()),
                ('water_meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_meter_readings', to='zhkh.watermeter')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='flat',
            unique_together={('house', 'number')},
        ),
    ]
