# Generated by Django 3.2.12 on 2022-03-14 09:42

import api.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', api.managers.UserManager()),
            ],
        ),
    ]