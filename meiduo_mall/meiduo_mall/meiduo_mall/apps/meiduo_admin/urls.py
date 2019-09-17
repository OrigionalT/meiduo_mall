from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from meiduo_admin.views import users, statistical, channels, skus, spus, orders

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthorizeView.as_view()),
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),
    url(r'^users/$', users.UserInfoView.as_view()),
    # 频道管理
    url(r'^goods/channel_types/$', channels.ChannelTypesView.as_view()),
    # 频道管理
    url(r'^goods/categories/$', channels.ChannelCategoriesView.as_view()),
    # 图片管理
    url(r'^skus/simple/$', skus.SKUSimpleView.as_view()),
    # SKU商品管理
    url(r'^goods/simple/$', spus.SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$', spus.SPUSpecView.as_view()),
]

router = DefaultRouter()
router.register('goods/channels', channels.ChannelViewSet, base_name='channels')
router.register(r'skus/images', skus.SKUImageViewSet, base_name='images')
router.register('skus', skus.SKUViewSet, base_name='skus')
router.register('orders', orders.OrdersViewSet, base_name='orders')
# router.register('goods', spus.SPUSpecView, base_name='specs')
urlpatterns += router.urls
