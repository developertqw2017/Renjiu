# Generated by Django 2.1 on 2018-08-10 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0008_auto_20180810_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupons',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]
