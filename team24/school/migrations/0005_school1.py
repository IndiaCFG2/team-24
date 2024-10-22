# Generated by Django 3.0.7 on 2020-08-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20200808_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='school1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=60)),
                ('school', models.CharField(max_length=100)),
                ('fee', models.CharField(blank=True, max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('teachers', models.IntegerField()),
                ('students', models.IntegerField()),
                ('date', models.CharField(max_length=60)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
