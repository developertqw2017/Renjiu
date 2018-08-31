from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
import random
import time
from uuid import uuid4
from datetime import datetime

from .datasettings import league_model as m_set
# Create your models here.

class DriverSchool(models.Model):
    province_id = models.IntegerField(verbose_name = '省', default = 0)
    #PROVINCE = ((0,'beijin'),)
    #CITY = ((0,'beijin'),(1,"shanghai"))
    city_id = models.IntegerField(verbose_name = '城市', default = 0)
    #DISTRICT = ((0,'beijin'))
    district_id = models.IntegerField(verbose_name = '区', default = 0)
    name = models.CharField(verbose_name = '店铺名称', max_length = 30)
    address = models.CharField(verbose_name='地址', max_length=100,blank = True, null = True)
    phone = models.CharField(verbose_name = '联系电话', max_length=50, blank = True, null = True)
    introduce = models.TextField(verbose_name='驾校介绍')
    characteristic = models.TextField(verbose_name = '驾校特色')
    sort = models.IntegerField(verbose_name = '排序')
    pic = models.ForeignKey('Icon', verbose_name='驾校商标', on_delete = models.DO_NOTHING)
    activity = models.CharField(verbose_name = '打折优惠信息', max_length=255)
    latitude = models.FloatField(verbose_name = '纬度')
    longitude = models.FloatField(verbose_name = '经度')
    number_good_reputation = models.IntegerField(verbose_name = '好评数')
    number_order = models.IntegerField(verbose_name = '订单数')

    class Meta:
        db_table = 'DriverSchool'
        verbose_name = '驾校'
        verbose_name_plural = '驾校'
        _order = 'sort'

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return self.name


class WechatUser(AbstractUser):
    cookie = models.CharField('用户认证标识', max_length=100,default='', blank = True)
    name = models.CharField(verbose_name = '昵称', max_length = 40, blank = True)
    openid = models.CharField(verbose_name = 'OpenId', max_length = 255, blank = True)
    union_id = models.CharField(verbose_name = 'UnionId', max_length = 255, blank = True)
    gender = models.SmallIntegerField(verbose_name = 'gender',default = 0, blank = True)
    language = models.CharField(verbose_name = '语言', max_length = 40, blank = True)
    #REGISTERTYPE = ((0,"beijin"))
    register_type = models.SmallIntegerField( verbose_name='注册来源',
                                     default=0)
    phone = models.CharField(verbose_name = '手机号码', max_length = 50, blank = True)
    #COUNTRY = ((0,"beijin"))
    country = models.IntegerField(verbose_name = '国家', default = 0, blank = True) 
    #PROVINCE = ((0,"beijin"))
    province = models.IntegerField(verbose_name = '省份', default = 0)
    #CITY = ((0,"beijin"))
    city = models.IntegerField(verbose_name = '城市', default = 0)
    avatar = models.ForeignKey('Icon', verbose_name='头像', on_delete = models.DO_NOTHING)
    register_ip = models.CharField(verbose_name = '注册IP', max_length = 80, blank = True)
    #last_login = models.DateTimeField(verbose_name = '登陆时间')
    ip = models.CharField(verbose_name = '登陆IP', max_length = 80, blank = True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'WechatUser'
        verbose_name = '微信用户'
        verbose_name_plural = '微信用户'

    def natural_key(self):
        return {"url":"https://qgdxsw.com:8000"+self.avatar.display_pic.url,"name":self.name}


class Goods(models.Model):
    category_id = models.ForeignKey('Category', on_delete = models.SET_DEFAULT, default = 0)
    characteristic = models.CharField(verbose_name = "描述", max_length = 100, default = '')
    dateAdd = models.DateTimeField(verbose_name = '上架时间', auto_now_add = True)
    dateStart = models.DateTimeField(verbose_name = '上架时间', auto_now_add = True)
    dateUpdate = models.DateTimeField(verbose_name = '更新时间', auto_now = True)
    logistics_id = models.IntegerField(verbose_name = '物流id', default = 0)
    minScore = models.SmallIntegerField(verbose_name = '最小评分', default = 0)
    name = models.CharField(verbose_name = '名称', max_length = 60)
    numberFav = models.IntegerField(verbose_name = "收藏人数",default = 0)
    numberGoodReputation = models.IntegerField(verbose_name = "好评数量",default = 0)
    numberOrders = models.IntegerField(verbose_name = '已售数量',default = 0)
    originalPrice = models.FloatField(verbose_name = "原价")
    paixu = models.IntegerField(default = 0)
    pic = models.ForeignKey('Icon', verbose_name = "商品图片连接", on_delete = models.SET_DEFAULT, default = 0)
    pingtuan = models.BooleanField(verbose_name = "拼团" , default = False)
    recommendStatus = models.SmallIntegerField(verbose_name = "推荐状态", default = 0)
    shop_id = models.ForeignKey("DriverSchool",verbose_name = "商店id", on_delete = models.CASCADE)
    status = models.SmallIntegerField(verbose_name  = "商品状态", default = 0)
    stores = models.IntegerField(verbose_name = "库存")
    video_id = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    weight = models.FloatField(default = 0.00)
    atomic = False

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.name

    def natural_key(self):
        return {"category_id":self.category_id,
                "characteristic":self.characteristic,
                "dateAdd":self.dateAdd,
                "dateStart":self.dateStart,
                "dateUpdate":self.dateUpdate,
                "logistics_id":self.logistics_id,
                "minScore":self.minScore,
                "name":self.name,
                "numberFav":self.numberFav,
                "numberGoodReputation":self.numberGoodReputation,
                "numberOrders":self.numberOrders,
                "originalPrice":self.originalPrice,
                "paixu":self.paixu,
                "pic":self.pic,
                "pingtuan":self.pingtuan,
                "recommendStatus":self.recommendStatus,
                "shop_id":self.shop_id,
                "status":self.status,
                "stores":self.stores,
                "video_id":self.video_id,
                "views":self.views,
                "weight":self.weight}

class Order(models.Model):
    wechat_user_id = models.ForeignKey('WechatUser', verbose_name ='微信用户', on_delete = models.DO_NOTHING)
    number_goods = models.IntegerField(verbose_name = '商品数量',default = 0)
    goods_price = models.FloatField(verbose_name = '商品总金额', default=0)
    logistics_id = models.ForeignKey('Logistics',verbose_name = '物流id', on_delete = models.SET_DEFAULT, default = 0)
    logistics_price = models.FloatField(verbose_name = '物流费用', default=0)
    total = models.FloatField('实际支付', default=0 )
    ORDER_STATUS = [(0,"待付款"),(1,'待发货'),(2,'待收货'),(3,'待评价'),(4,'已完成'),(5,'已删除')]
    status = models.SmallIntegerField(verbose_name = '状态', choices = ORDER_STATUS, default = 0)
    remark = models.CharField(verbose_name  = '备注', max_length = 100, blank = True)
    linkman = models.CharField(verbose_name = '联系人', max_length = 100, blank = True)
    phone = models.CharField(verbose_name = '手机号码', max_length = 50, blank = True)
    #PROVINCE = ((0,"22"))
    province_id = models.SmallIntegerField(verbose_name='省', default = 0)
    #CITY = ((0,"22"))
    city_id = models.SmallIntegerField(verbose_name = '市', default = 0)
    district_id = models.SmallIntegerField(verbose_name = '区', default = 0)
    address = models.CharField(verbose_name = '详细地址', max_length = 100, blank = True)
    postcode = models.CharField(verbose_name = '邮政编码', max_length = 20, blank = True)
    shipper_id = models.ForeignKey('Shipper', verbose_name='快递承运商', on_delete = models.DO_NOTHING, default = 1)
    tracking_number = models.CharField(verbose_name = '运单号', max_length = 200, blank = True)
    #display_traces = fields.Html('物流信息', compute='_compute_display_traces')
    traces = models.TextField(verbose_name = '物流信息', blank = True)
    dateAdd = models.DateTimeField(verbose_name = '下单时间', default = timezone.now)

    class Meta:
        db_table = 'Order'
        verbose_name = '订单'
        verbose_name_plural = '订单'
 
    #payment_ids = fields.One2many('wechat_mall.payment', 'order_id', '支付记录')
    def __str__(self):
        return "{0}".format(self.id)

    def natural_key(self):
        return {"wechat_user_id":self.wechat_user_id,
                "number_goods":self.number_goods,
                "goods_price":self.goods_price,
                "logistics_id":self.logistics_id,
                "logistics_price":self.logistics_price,
                "total":self.total,
                "status":self.get_status_display,
                "remark":self.remark,
                "linkman":self.linkman,
                "phone":self.phone,
                "province_id":self.province_id,
                "city_id":self.city_id,
                "district_id":self.district_id,
                "address":self.address,
                "postcode":self.postcode,
                "shipper_id":self.shipper_id,
                "tracking_number":self.tracking_number,
                "traces":self.traces,
                "dateAdd":self.dateAdd}


class OrderGoods(models.Model):
    order_id = models.IntegerField(verbose_name='订单', default = 0)
    # 冗余记录商品，防止商品删除后订单数据不完整
    goods_id = models.IntegerField(verbose_name = '商品id',default = 0)
    name = models.CharField(verbose_name = '商品名称', max_length = 50, blank =True)
    display_pic = models.ForeignKey('Icon',verbose_name = '图片', on_delete = models.SET_DEFAULT, default = 0)
    property_str = models.CharField(verbose_name = '商品规格', max_length = 200, blank = True)
    price = models.FloatField(verbose_name = '单价', default = 0)
    amount = models.IntegerField(verbose_name = '商品数量', default = 0)
    total = models.FloatField(verbose_name = '总价', default = 0)
    
    class Meta:
        db_table = 'OrderGoods'
        verbose_name = '订单商品'
        verbose_name_plural = '订单商品'

    def __str__(self):
        return self.name

    def natural_key(self):
        return {"order_id":self.order_id,
                "goods_id":self.goods_id,
                "name":self.name,
                "display_pic":self.display_pic,
                "property_str":self.property_str,
                "price":self.price,
                "amount":self.amount,
                "total":self.total}


class ModifyPriceWizard(models.Model):
    order_id = models.ForeignKey('Order', verbose_name ='订单', on_delete = models.CASCADE)
    total = models.FloatField(verbose_name = '金额')

    class Meta:
        db_table = 'ModifyPriceWizard'
        verbose_name = '修改价格'
        verbose_name_plural = '修改价格'

    def natural_key(self):
        return {"order_id":self.order_id,
                "total":self.total}


class DeliverWizard(models.Model):
    _name = 'wechat_mall.deliver.wizard'
    order_id = models.ForeignKey('Order', verbose_name='订单', on_delete = models.CASCADE)
    shipper_id = models.ForeignKey('Shipper', verbose_name='快递承运商', on_delete = models.CASCADE)
    tracking_number = models.CharField(verbose_name = '运单号', max_length = 200)
    status = models.CharField(verbose_name = '状态', max_length = 20)

    class Meta:
        db_table = 'DeliverWizard'
        _description = '发货'

    def natural_key(self):
        return {"order_id":self.order_id,
                "shipper_id":self.shipper_id,
                "tracking_number":self.tracking_number,
                "status":self.status}


class Shipper(models.Model):
    name =  models.CharField(verbose_name = '名称', max_length = 50)
    code = models.CharField(verbose_name = '编码', max_length = 100)

    class Meta:
        db_table = 'Shipper'
        verbose_name = '承运商'
        verbose_name_plural = '承运商'

    def __str__(self):
        return self.name

    def natural_key(self):
        return {"name":self.name,
                "code":self.code}


class Logistics(models.Model):
    name = models.CharField('名称', max_length = 50)
    by_self = models.BooleanField(verbose_name = '商家配送', default = False)
    free = models.BooleanField(verbose_name = '是否包邮', default = False)
    #LogisticsValuationType = ((0,"22"))
    valuation_type = models.SmallIntegerField(verbose_name='计价方式'
                                      ,default=0)

    class Meta:
        db_table = 'Logistics'
        verbose_name = '物流信息'
        verbose_name_plural = '物流信息'
    
    def __str__(self):
        return self.name

    def natural_key(self):
        return {"name":self.name,
                "by_self":self.name,
                "free":self.free,
                "valuation_type":self.valuation_type}


class Category(models.Model):
    name = models.CharField(verbose_name='名称', max_length = 100)
    eng_name = models.CharField(verbose_name = '名称(英文)', max_length = 100)
    category_type = models.CharField(verbose_name = '类型',max_length = 30)
    pid = models.ForeignKey('Category', verbose_name='上级分类', on_delete = models.SET_DEFAULT, default = 0)
    key = models.IntegerField(verbose_name='编号')
    icon = models.ForeignKey('Icon', verbose_name='图标', on_delete = models.CASCADE)
    level = models.SmallIntegerField(verbose_name='分类级别')
    is_use = models.BooleanField(verbose_name='是否启用', default=True)
    sort = models.IntegerField(verbose_name='排序')
    
    class Meta:
        db_table = 'Category'
        verbose_name = '商品分类'
        verbose_name_plural = '商品分类'
        _order = 'level,sort'
    def __str__(self):
        return self.name

    def natural_key(self):
        return {"name":self.name,
                "eng_name":self.eng_name,
                "category_type":self.category_type,
                "pid":self.pid,
                "key":self.key,
                "icon":self.icon,
                "level":self.level,
                "is_use":self.is_use,
                "sort":self.sort}

def filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    year = datetime.now().year
    month =datetime.now().month
    day = datetime.now().day
    return "img/{0}/{1}/{2}/{3}".format(year,month,day,filename)

class Icon(models.Model):
   name = models.CharField(verbose_name = "图标名称", max_length = 20)
   display_pic = models.ImageField(verbose_name = "icon 对应",upload_to=filepath)
    
   class Meta:
       db_table = 'Icon'
       verbose_name = '图标'
       verbose_name_plural = '图标'

   def __str__(self):
       return self.name


class Attachment(models.Model):
    
    display_pic = models.ImageField(verbose_name = "附件图片",upload_to=filepath)
    owner_id = models.ForeignKey("Goods",verbose_name = "所属货物", on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'Attachment'
        verbose_name = '图片'
        verbose_name_plural = '图片'

    def __str__(self):
        return self.owner_id.name


class Payment(models.Model):

    order_id = models.ForeignKey('Order', verbose_name = '订单', on_delete = models.CASCADE)
    payment_number = models.CharField(verbose_name = '支付单号', max_length = 255)
    wechat_user_id = models.ForeignKey('WechatUser', verbose_name = '微信用户', on_delete = models.DO_NOTHING)
    price = models.FloatField(verbose_name = '支付金额(元)')
    #PAYMENT_STATUS = ((0,"22"))
    status = models.SmallIntegerField(verbose_name = '状态', choices = m_set.PAYMENT_STATUS, default=1)
    # 微信notify返回参数
    openid = models.CharField(verbose_name = 'openid', max_length = 255)
    result_code = models.CharField(verbose_name = '业务结果', max_length = 30)
    err_code = models.CharField(verbose_name = '错误代码', max_length = 40)
    err_code_des = models.CharField(verbose_name = '错误代码描述', max_length = 255)
    transaction_id = models.CharField(verbose_name = '微信订单号', max_length = 255)
    bank_type = models.CharField(verbose_name = '付款银行', max_length = 50)
    fee_type = models.CharField(verbose_name = '货币种类', max_length = 20)
    total_fee = models.FloatField(verbose_name = '订单金额(分)')
    settlement_total_fee = models.FloatField(verbose_name = '应结订单金额(分)')
    cash_fee = models.FloatField(verbose_name = '现金支付金额')
    cash_fee_type = models.CharField(verbose_name = '现金支付货币类型', max_length = 40)
    coupon_fee = models.FloatField(verbose_name = '代金券金额(分)')
    coupon_count = models.IntegerField(verbose_name = '代金券使用数量')

    class Meta:
        db_table = 'Payment'
        verbose_name = '支付记录'
        verbose_name_plural = '支付记录'

    def __str__(self):
        return self.id

    def natural_key(self):
        return {"order_id":self.order_id,
                "payment_number":self.payment_number,
                "wechat_user_id":self.wechat_user_id,
                "price":self.price,
                "status":self.get_status_display,
                "openid":self.openid,
                "result_code":self.result_cde,
                "err_code":self.err_code,
                "err_code_des":self.err_code_des,
                "transaction_id":self.transaction_id,
                "bank_type":self.bank_type,
                "fee_type":self.fee_type,
                "total_fee":self.total_fee,
                "settlement_total":self.settlement_total,
                "cash_fee":self.cash_fee,
                "cash_fee_type":self.cash_fee_type,
                "coupon_fee":self.coupon_fee,
                "coupon_count":self.coupon_count}


class Address(models.Model):
    province_id = models.IntegerField(verbose_name = '省', default = 0)
    #PROVINCE = ((0,'beijin'),)
    #CITY = ((0,'beijin'),(1,"shanghai"))
    city_id = models.IntegerField(verbose_name = '城市', default = 0)
    #DISTRICT = ((0,'beijin'))
    district_id = models.IntegerField(verbose_name = '区', default = 0)
    linkMan = models.CharField(verbose_name = '联系人', max_length = 15)
    address = models.CharField(verbose_name = '详细地址', max_length = 100)
    mobile = models.CharField(verbose_name = '电话号码', max_length = 40)
    code = models.CharField(verbose_name = '邮政编码', max_length = 20)
    isDefault = models.BooleanField(verbose_name = '默认地址',default = False)
    owner_type = models.SmallIntegerField(verbose_name = "被标注地址的类型eg:微信用户,订单")
    owner_id = models.IntegerField(verbose_name = "微信用户、订单的id")

    class Meta:
        db_table = 'Address'
        verbose_name = '地址'
        verbose_name_plural = '地址'

    def natural_key(self):
        return {"province_id":self.province_id,
                "city_id":self.city_id,
                "district_id":self.district_id,
                "linkMan":self.linkMan,
                "address":self.address,
                "mobile":self.mobile,
                "code":self.code,
                "isDefault":self.isDefault,
                "owner_type":self.owner_type,
                "owner_id":self.owner_id}


class Coupons(models.Model):
    name = models.CharField(verbose_name = '优惠券名称', max_length = 50)
    moneyMin = models.FloatField(verbose_name = '优惠券金额')
    moneyHreshold = models.FloatField(verbose_name = '满 减 最低额度')
    DATE_END_TYPE = ((0,"截止某日前有效"),(1,"领取后有效时间倒计"))
    dateEndType = models.SmallIntegerField(verbose_name = '优惠券有效期类型', choices = DATE_END_TYPE)
    dateEndDays = models.DateTimeField(verbose_name = "优惠券截止时间", default = timezone.now)
    goods_id =  models.ForeignKey('Goods', on_delete = models.CASCADE, verbose_name = "商品id")
    is_active = models.BooleanField(verbose_name = "优惠券是否有效")
    date_add = models.DateTimeField(verbose_name = "优惠券添加的时间", default = timezone.now)
    coupons_type = models.SmallIntegerField(verbose_name = "优惠券类型1.通用型,2.分类专用型,3.商品专用型,4.店铺专用型", default = 0)

    class Meta:
        db_table = 'Coupons'
        verbose_name = "优惠券"
        verbose_name_plural = "优惠券"

    def __str__(self):
        return self.name

    def natural_key(self):
        return {"name":self.name,
                "moneyMin":self.moneyMin,
                "moneyHreshold":self.moneyHreshold,
                "dateEndType":self.get_dateEndType_display,
                "goods_id":self.goods_id,
                "is_active":self.is_active,
                "date_add":self.date_add,
                "coupons_type":self.coupons_type}



class Coupons_users(models.Model):
    coupons_id = models.IntegerField(verbose_name = "优惠券id")
    user_id = models.IntegerField(verbose_name = "用户id")
    date_add = models.DateTimeField(verbose_name = "优惠券添加的时间", default = timezone.now)
    dateEndDays = models.DateTimeField(verbose_name = "优惠券截止时间", default = timezone.now)

    class Meta:
        db_table = 'Coupons_users'
        verbose_name = "用户领取的优惠券"
        verbose_name_plural = "用户领取的优惠券"

    def __str__(self):
        return self.id

    def natural_key(self):
        return {"coupons_id":self.coupons_id,
                "user_id":self.user_id,
                "date_add":self.date_add,
                "dateEndDays":self.dateEndDays}


class Book(models.Model):
    coach = models.ForeignKey('WechatUser', on_delete = models.CASCADE, verbose_name = "教练id")
    train_ground = models.ForeignKey('DriverSchool', on_delete = models.CASCADE, verbose_name = "训练场id")
    length_time = models.FloatField(verbose_name = "预约时间长度")
    book_time_start = models.IntegerField(verbose_name = "预约开始时间",default = datetime.now)
    book_time_end = models.IntegerField(verbose_name = "预约结束时间", default = datetime.now)
    last_active_time = models.DateTimeField('最近操作时间', auto_now=True)
    status = models.SmallIntegerField(verbose_name = '预约状态')
    
    class Meta:
        db_table = 'Book'
        verbose_name = '学员教练预约'
        verbose_name_plural = "学员教练预约"

    def __str__(self):
        return "教练"
    
    def natural_key(self):
        return {"coach":self.coach,
                "train_ground":self.train_ground,
                "length_time":self.length_time,
                "book_time_start":self.book_time_start,
                "book_time_end":self.book_time_end,
                "last_active_end":self.last_active_time,
                "status":self.status}


class Bargain(models.Model):
    goods_id = models.ForeignKey('Goods', on_delete = models.CASCADE, verbose_name = '货物')
    times = models.IntegerField(verbose_name = '砍价次数', default = 0)

    price = models.FloatField(verbose_name = '砍价当前价格')
    minPrice = models.FloatField(verbose_name = '砍价最低价格')
    calculate_method = models.SmallIntegerField(verbose_name = '砍价计算模式', choices = m_set.BARGAIN_CALCULATE_METHOD, max_length = 50)
    expected_price = models.FloatField(verbose_name = '期望砍价价格') 
    expected_times = models.FloatField(verbose_name = '期望砍价次数') 
    date_start = models.DateTimeField(verbose_name = '活动开始时间',auto_now_add = True)
    date_end = models.DateTimeField(verbose_name = '活动结束时间')

    class Meta:
        db_table = 'Bargain'
        verbose_name = '砍价'
        verbose_name_plural = '砍价'

    def __str__(self):
        return self.goods_id.name

    def natural_key(self):
        return {"id":self.id,
                "goods_id":self.goods_id,
                "times":self.times,
                "price":self.price,
                "minPrice":self.minPrice,
                "caculate_method":self.get_calculate_method_display,
                "expected_price":self.expected_price,
                "expected_times":self.expected_times,
                "date_start":self.date_start,
                "date_end":self.date_end}


class BargainUser(models.Model):
    bargain_id = models.ForeignKey('Bargain', on_delete = models.CASCADE, verbose_name = '砍价活动')
    user_id = models.ForeignKey('WechatUser', on_delete = models.CASCADE, verbose_name = '砍价用户')
    bargain_date = models.DateTimeField(verbose_name = "砍价发起时间", auto_now_add = True)
    class Meta:
        db_table = 'BargainUser'
        verbose_name = '砍价用户记录'
        verbose_name_plural = '砍价用户记录'

    def __str__(self):
        return self.bargain_id.goods_id.name+self.user_id.name

    def natural_key(self):
        return {"id":self.id,"bargain_id":bargain_id,"user_id":user_id}


class BargainFriend(models.Model):
    bargainUser_id = models.ForeignKey('BargainUser', on_delete = models.CASCADE, verbose_name = '砍价发起用户')
    bargainFriend_id = models.ForeignKey('WechatUser', on_delete = models.CASCADE, verbose_name = '参与砍价好友')


class GoodsReputation(models.Model):
    goods_id = models.ForeignKey('Goods', on_delete = models.CASCADE, verbose_name = '商品')
    user_id = models.ForeignKey('WechatUser', on_delete = models.DO_NOTHING, verbose_name = '评论用户')
    goods_reputation_str = models.CharField(verbose_name = "评价级别", max_length = 20)
    goods_reputation_remark = models.TextField(verbose_name = "评论备注")
    dates_reputation = models.DateTimeField(verbose_name = "评论日期",auto_now_add = True)

    class Meta:
        db_table = 'GoodsReputation'
        verbose_name = '商品评论'
        verbose_name_plural = '商品评论'
    
    def __str__(self):
        return self.goods_id.name

    def natural_key(self):
        return {"id":self.id,
                "goods_id":self.user_id,
                "goods_reputation_str":self.goods_reputation_str,
                "goods_reputation_remark":self.goods_reputation_remark,
                "dates_reputation":self.dates_reputation}
