# Generated by Django 3.0.5 on 2020-04-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200414_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessages',
            options={'ordering': ['id']},
        ),
    ]