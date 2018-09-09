# Generated by Django 2.1 on 2018-08-31 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0050_auto_20180831_2131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bargainfriend',
            options={'verbose_name': '帮忙砍价的好友', 'verbose_name_plural': '帮忙砍价的好友'},
        ),
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
        migrations.AlterModelTable(
            name='bargainfriend',
            table='BargainFriend',
        ),
    ]