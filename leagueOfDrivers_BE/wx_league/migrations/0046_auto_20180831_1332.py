# Generated by Django 2.1 on 2018-08-31 13:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wx_league', '0045_auto_20180831_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='BargainFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='bargain',
            name='date_end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='活动结束时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bargain',
            name='date_start',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='活动开始时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bargainuser',
            name='bargain_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='砍价发起时间'),
            preserve_default=False,
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
        migrations.AddField(
            model_name='bargainfriend',
            name='bargainUser_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wx_league.BargainUser', verbose_name='砍价发起用户'),
        ),
    ]