# Generated by Django 3.0.5 on 2020-04-10 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200410_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizations',
            options={'ordering': ['organization_name']},
        ),
        migrations.AlterModelOptions(
            name='players',
            options={'ordering': ['organization_level']},
        ),
    ]