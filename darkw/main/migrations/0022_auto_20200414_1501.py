# Generated by Django 3.0.5 on 2020-04-14 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_chatmessages_room_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessages',
            options={'ordering': ['-id']},
        ),
    ]
