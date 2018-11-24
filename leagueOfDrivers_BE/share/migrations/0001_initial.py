<<<<<<< HEAD
# Generated by Django 2.1.2 on 2018-11-22 10:23
=======
# Generated by Django 2.1.2 on 2018-11-19 13:41
>>>>>>> f732481b08b46fe49ae469347944bf5ec8ca3422

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wx_league', '0093_auto_20181122_1023'),
=======
        ('wx_league', '0096_auto_20181119_1341'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> f732481b08b46fe49ae469347944bf5ec8ca3422
    ]

    operations = [
        migrations.CreateModel(
            name='RebateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(verbose_name='佣金')),
                ('level', models.SmallIntegerField(verbose_name='获佣级别')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='获得佣金时间')),
                ('confirm', models.DateTimeField(blank=True, null=True, verbose_name='确认收钱时间')),
                ('status', models.SmallIntegerField(choices=[(0, '未付款'), (1, '已付款'), (2, '等待分成(已收货)'), (3, '已分成'), (4, '已取消')], verbose_name='佣金状态')),
                ('confirm_time', models.DateTimeField(verbose_name='确认分成或者取消时间')),
                ('remark', models.CharField(blank=True, max_length=200, null=True, verbose_name='取消备注')),
                ('buy_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rebatelog_buy_u', to=settings.AUTH_USER_MODEL, verbose_name='购买用户')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rebatelog_o', to='wx_league.Order', verbose_name='订单')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx_league.DriverSchool', verbose_name='店铺')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rebatelog_u', to=settings.AUTH_USER_MODEL, verbose_name='获佣用户')),
            ],
        ),
        migrations.CreateModel(
            name='ShareGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_times', models.IntegerField(verbose_name='分享次数')),
                ('sales_num', models.IntegerField(verbose_name='分销销量')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='加入分销时间')),
                ('goods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx_league.Goods', verbose_name='分销商品')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wx_league.DriverSchool', verbose_name='商店')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='商品所属用户')),
            ],
        ),
        migrations.CreateModel(
            name='ShareUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_f_leader', to=settings.AUTH_USER_MODEL, verbose_name='第一个上级')),
                ('second_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_s_leader', to=settings.AUTH_USER_MODEL, verbose_name='第二个上级')),
                ('third_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_t_leader', to=settings.AUTH_USER_MODEL, verbose_name='第三个上级')),
<<<<<<< HEAD
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='share_user', to=settings.AUTH_USER_MODEL, verbose_name='分销用户')),
=======
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_user', to=settings.AUTH_USER_MODEL, verbose_name='分销用户')),
>>>>>>> f732481b08b46fe49ae469347944bf5ec8ca3422
            ],
        ),
    ]
