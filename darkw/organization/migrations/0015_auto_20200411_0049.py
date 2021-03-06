# Generated by Django 3.0.5 on 2020-04-10 22:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0014_organizationranks_rank_power'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationranks',
            options={'ordering': ['-rank_power']},
        ),
        migrations.AlterField(
            model_name='organizationranks',
            name='rank_power',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
