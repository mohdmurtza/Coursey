# Generated by Django 3.2.16 on 2023-01-28 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='city',
            new_name='country',
        ),
    ]
