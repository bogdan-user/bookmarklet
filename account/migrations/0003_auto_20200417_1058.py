# Generated by Django 3.0.5 on 2020-04-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_form',
            new_name='user_from',
        ),
    ]
