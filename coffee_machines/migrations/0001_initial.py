# Generated by Django 3.1.1 on 2020-09-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeMachines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('machine_type', models.CharField(choices=[('S', 'Small Coffee Machine'), ('L', 'Large Coffee Machine'), ('E', 'Espresso Machine')], default='S', max_length=1)),
                ('machine_class', models.CharField(choices=[('B', 'Base Model'), ('P', 'Premium Model'), ('D', 'Deluxe Model')], default='B', max_length=1)),
            ],
        ),
    ]
