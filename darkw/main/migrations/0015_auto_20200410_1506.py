# Generated by Django 3.0.5 on 2020-04-10 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0013_delete_organization'),
        ('main', '0014_organizations_default_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='default_rank',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='default_rank', to='organization.OrganizationRanks'),
        ),
    ]
