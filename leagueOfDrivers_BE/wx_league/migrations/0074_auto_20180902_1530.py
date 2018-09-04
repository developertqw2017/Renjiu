# Generated by Django 2.1 on 2018-09-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0073_auto_20180902_1525'),
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
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='详细地址'),
        ),
        migrations.AlterField(
            model_name='order',
            name='linkman',
            field=models.CharField(default='', max_length=100, verbose_name='联系人'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=50, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='', max_length=20, verbose_name='邮政编码'),
        ),
        migrations.AlterField(
            model_name='order',
            name='remark',
            field=models.CharField(default='', max_length=100, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='order',
            name='traces',
            field=models.TextField(default='', verbose_name='物流信息'),
        ),
    ]
