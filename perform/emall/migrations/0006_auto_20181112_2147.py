# Generated by Django 2.1.3 on 2018-11-12 13:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('emall', '0005_auto_20181112_0846'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('sorted_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
