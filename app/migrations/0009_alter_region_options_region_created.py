# Generated by Django 5.0.3 on 2024-05-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_region_population'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='region',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]