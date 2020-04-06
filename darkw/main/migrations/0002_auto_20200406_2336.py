# Generated by Django 3.0.5 on 2020-04-06 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='organization_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.OrganizationRanks'),
        ),
        migrations.AddField(
            model_name='organizations',
            name='boss',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Players'),
        ),
    ]