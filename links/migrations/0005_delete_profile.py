# Generated by Django 3.2.13 on 2022-04-26 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('links', '0004_auto_20220426_1430'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile',
        ),
    ]
