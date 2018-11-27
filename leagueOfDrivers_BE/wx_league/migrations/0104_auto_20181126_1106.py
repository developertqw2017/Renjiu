# Generated by Django 2.1.2 on 2018-11-26 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0103_auto_20181126_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wx_league.Goods', verbose_name='所属货物'),
        ),
        migrations.AlterField(
            model_name='bargain',
            name='goods_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wx_league.Goods', verbose_name='货物'),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='goods_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wx_league.Goods', verbose_name='商品id'),
        ),
        migrations.AlterField(
            model_name='goodsreputation',
            name='goods_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wx_league.Goods', verbose_name='商品'),
        ),
    ]