# Generated by Django 3.0.5 on 2020-04-09 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200408_2234'),
        ('organization', '0009_auto_20200410_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invites',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Organizations'),
        ),
    ]
