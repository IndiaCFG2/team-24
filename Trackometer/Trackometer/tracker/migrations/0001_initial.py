# Generated by Django 3.0.2 on 2020-08-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonCPD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tech', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
