# Generated by Django 5.0.1 on 2025-03-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='datepublic',
            field=models.DateField(),
        ),
    ]
