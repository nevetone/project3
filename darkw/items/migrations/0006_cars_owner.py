# Generated by Django 3.0.5 on 2020-04-08 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200408_2234'),
        ('items', '0005_cars_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Players'),
        ),
    ]
