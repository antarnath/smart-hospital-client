# Generated by Django 5.0.4 on 2024-07-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='number_of_patients',
            field=models.IntegerField(default=0),
        ),
    ]
