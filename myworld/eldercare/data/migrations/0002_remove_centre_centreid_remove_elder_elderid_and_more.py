# Generated by Django 4.2.3 on 2023-07-10 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centre',
            name='centreid',
        ),
        migrations.RemoveField(
            model_name='elder',
            name='elderid',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicleid',
        ),
    ]
