# Generated by Django 3.0.5 on 2020-04-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200414_1504'),
        ('organization', '0015_auto_20200411_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invites',
            name='players',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Players'),
        ),
    ]