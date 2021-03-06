# Generated by Django 3.0.5 on 2020-04-12 22:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0019_auto_20200411_0049'),
        ('items', '0007_delete_organizationitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(choices=[('Pranie', 'Pranie'), ('Kontrabanda', 'Kontrabanda'), ('Sprzedaż', 'Sprzedaż')], max_length=50)),
                ('status', models.CharField(choices=[('Oczekujący', 'Oczekujący'), ('W trakcie', 'W trakcie'), ('Zakończone', 'Zakończone')], default='Oczekujący', max_length=50)),
                ('if_pranie', models.IntegerField(default=5000, validators=[django.core.validators.MaxValueValidator(30000), django.core.validators.MinValueValidator(5000)])),
                ('if_pranie_prowizja', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('if_kontrabanda_or_sprzedaz', models.ManyToManyField(to='items.PlayerItems')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Players')),
            ],
        ),
    ]
