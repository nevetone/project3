# Generated by Django 3.0.5 on 2020-04-13 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200411_0049'),
        ('orders', '0006_orders_received'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ordered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_by', to='main.Players'),
        ),
    ]
