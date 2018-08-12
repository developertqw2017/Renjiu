var app = getApp();
Page({
    data:{
      orderId:0,
        goodsList:[
            {
                pic:'/images/goods02.png',
                name:'爱马仕（HERMES）大地男士最多两行文字超出就这样显…',
                price:'300.00',
                label:'大地50ml',
                number:2
            },
            {
                pic:'/images/goods02.png',
                name:'爱马仕（HERMES）大地男士最多两行文字超出就这样显…',
                price:'300.00',
                label:'大地50ml',
                number:2
            }
        ],
        yunPrice:"10.00"
    },
    onLoad:function(e){
      var orderId = e.id;
      this.data.orderId = orderId;
      this.setData({
        orderId: orderId
      });
    },
    onShow : function () {
      var that = this;
      wx.request({
        url: app.globalData.baseUrl + '/order/detail',
        data: {
          cookie: app.globalData.cookie,
          id: that.data.orderId
        },
        success: (res) => {
          wx.hideLoading();
          if (res.data.code != 0) {
            wx.showModal({
              title: '错误',
              content: res.data.msg,
              showCancel: false
            })
            return;
          }
          that.setData({
            orderDetail: res.data.data
          });
        }
      })
      var yunPrice = parseFloat(this.data.yunPrice);
      var allprice = 0;
      var goodsList = this.data.goodsList;
      for (var i = 0; i < goodsList.length; i++) {
        allprice += parseFloat(goodsList[0].price) * goodsList[0].number;
      }
      this.setData({
        allGoodsPrice: allprice,
        yunPrice: yunPrice
      });
    },
    wuliuDetailsTap:function(e){
      var orderId = e.currentTarget.dataset.id;
      wx.navigateTo({
        url: "/pages/wuliu/index?id=" + orderId
      })
    },
    confirmBtnTap:function(e){
      var that = this;
      var orderId = e.currentTarget.dataset.id;
      wx.showModal({
          title: '确认您已收到商品？',
          content: '',
          success: function(res) {
            if (res.confirm) {
              wx.showLoading();
              wx.request({
                url: app.globalData.baseUrl + '/order/delivery',
                data: {
                  cookie: app.globalData.cookie,
                  orderId: orderId
                },
                success: (res) => {
                  if (res.data.code == 0) {
                    that.onShow();
                  }
                }
              })
            }
          }
      })
    },
    submitReputation: function (e) {
      var that = this;
      var postJsonString = {};
      postJsonString.cookie = app.globalData.cookie;
      postJsonString.orderId = this.data.orderId;
      var reputations = [];
      var i = 0;
      while (e.detail.value["orderGoodsId" + i]) {
        var orderGoodsId = e.detail.value["orderGoodsId" + i];
        var goodReputation = e.detail.value["goodReputation" + i];
        var goodReputationRemark = e.detail.value["goodReputationRemark" + i];

        var reputations_json = {};
        reputations_json.id = orderGoodsId;
        reputations_json.reputation = goodReputation;
        reputations_json.remark = goodReputationRemark;

        reputations.push(reputations_json);
        i++;
      }
      postJsonString.reputations = reputations;
      wx.showLoading();
      wx.request({
        url: app.globalData.baseUrl + '/order/reputation',
        data: {
          postJsonString: postJsonString
        },
        success: (res) => {
          wx.hideLoading();
          if (res.data.code == 0) {
            that.onShow();
          }
        }
      })
    }
})