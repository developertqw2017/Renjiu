# Generated by Django 2.1 on 2018-08-09 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0002_remove_category_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='wx_league.Category', verbose_name='上级分类'),
        ),
    ]