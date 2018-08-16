var app = getApp();
// pages/product_list/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    page:1,
    hidden:true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    this.setData({
      id:options.id
    })
    this.getList();
  },
  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    this.getList();
  },
  getList(){
    var self = this;
    var _page = self.data.page;
    self.setData({
      hidden: false
    })
    console.log(self.data.id)
    //获取分类商品
    wx.request({
      url: 'https://qgdxsw.com:8000/league/goods/list',
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      method: "POST",
      data: {
        page: _page,
        pageSize: 6,
        categoryId: self.data.id
      },
      success: function (res) {
        console.log(res.data.data[0].fields.category_id)
        if (!res.data.data) {
          wx.showToast({
            title: res.data.msg
          })
          self.setData({
            hidden: true
          })
          return false
        }
        var second = app.globalData.tlist[0].second
        var en_name = "";
        for (var x in second)
        {
          console.log("ssssssssssssss"+second[x].pk, res.data.data[0].fields.category_id)
           if(second[x].pk == res.data.data[0].fields.category_id)
           {
             en_name = second[x].fields.eng_name;
           }
        }
        self.setData({
          en_name:en_name,
          page : _page+1,
          list: _page == 1 ? res.data.data : self.data.list.concat(res.data.data)
        });//当前页页数+1
        wx.hideNavigationBarLoading() //完成停止加载
        wx.stopPullDownRefresh() //停止下拉刷新
        console.log(en_name)
        self.setData({
          hidden: true
        })
      }
    })
  }
})