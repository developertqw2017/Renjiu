# Generated by Django 2.1.2 on 2018-11-22 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20181122_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharegoods',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx_league.Goods', verbose_name='分销商品'),
        ),
        migrations.AlterField(
            model_name='shareuserprofile',
            name='cash_price',
            field=models.FloatField(default=0, verbose_name='成功提现佣金'),
        ),
        migrations.AlterField(
            model_name='shareuserprofile',
            name='order_money',
            field=models.FloatField(default=0, verbose_name='分销订单'),
        ),
        migrations.AlterField(
            model_name='shareuserprofile',
            name='price',
            field=models.FloatField(default=0, verbose_name='可提现佣金'),
        ),
        migrations.AlterField(
            model_name='shareuserprofile',
            name='team_count',
            field=models.IntegerField(default=0, verbose_name='我的团队人数'),
        ),
        migrations.AlterField(
            model_name='shareuserprofile',
            name='total_cash',
            field=models.FloatField(default=0, verbose_name='分销佣金'),
        ),
        migrations.AlterField(
            model_name='shareuserprofile',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='最终'),
        ),
    ]