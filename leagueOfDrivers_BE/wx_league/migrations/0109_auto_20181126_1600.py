# Generated by Django 2.1.2 on 2018-11-26 16:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0108_auto_20181126_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechatuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wechatuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
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
    ]