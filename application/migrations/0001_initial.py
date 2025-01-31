# Generated by Django 5.0.6 on 2024-05-09 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.person')),
            ],
        ),
    ]
