# Generated by Django 2.1.3 on 2018-11-12 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emall', '0004_auto_20181111_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='logistics_id',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='number_fav',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='paixu',
        ),
    ]
