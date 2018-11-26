# Generated by Django 2.1.2 on 2018-11-26 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0011_auto_20181126_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shareordergoods',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='shareordergoods',
            name='goods_id',
        ),
        migrations.AddField(
            model_name='shareordergoods',
            name='goods',
            field=models.IntegerField(default=0, verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='sharegoods',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx_league.Goods', verbose_name='分销商品'),
        ),
    ]
