# Generated by Django 3.1.2 on 2020-10-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
