# Generated by Django 2.1.3 on 2018-11-14 03:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20181112_2147'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='indextopic',
            managers=[
                ('sorted_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]