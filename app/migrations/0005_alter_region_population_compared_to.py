# Generated by Django 5.0.3 on 2024-05-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_region_population_compared_to_alter_region_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='population_compared_to',
            field=models.DateField(null=True),
        ),
    ]