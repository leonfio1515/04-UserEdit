# Generated by Django 4.0.5 on 2023-05-28 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_alter_users_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='city',
        ),
    ]
