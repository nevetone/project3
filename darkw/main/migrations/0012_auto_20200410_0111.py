# Generated by Django 3.0.5 on 2020-04-09 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_players_invited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='invited',
            field=models.BooleanField(default=False),
        ),
    ]
