# Generated by Django 3.1.1 on 2020-09-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_machines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeemachines',
            name='water_line_compatiple',
            field=models.BooleanField(default=False),
        ),
    ]
