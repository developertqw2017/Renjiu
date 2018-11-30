# Generated by Django 2.1.3 on 2018-11-11 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsReputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_reputation_str', models.CharField(max_length=20, verbose_name='评价级别')),
                ('goods_reputation_remark', models.TextField(verbose_name='评论备注')),
                ('dates_reputation', models.DateTimeField(auto_now_add=True, verbose_name='评论日期')),
                ('goods_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emall.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='评论用户')),
            ],
            options={
                'verbose_name': '商品评论',
                'db_table': 'GoodsReputation',
                'verbose_name_plural': '商品评论',
            },
        ),
        migrations.CreateModel(
            name='Preferential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off', models.FloatField(verbose_name='打折折扣')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='特价商品生效时间')),
                ('date_end', models.DateTimeField(verbose_name='特价商品下架时间')),
                ('preferential_type', models.CharField(choices=[(0, 'preferentail'), (1, 'inventory'), (2, 'offer')], max_length=50)),
                ('goods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emall.Goods')),
            ],
        ),
    ]