# Generated by Django 3.1.2 on 2020-10-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
