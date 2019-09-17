from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serializer.orders import OrderListSerializer, OrderDetailSerializer
from orders.models import OrderInfo


class OrdersViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]

    serializer_class = OrderListSerializer

    def get_queryset(self):
        # 获取关键字
        keyword = self.request.query_params.get('keyword')

        if not keyword:
            orders = OrderInfo.objects.all()
        else:
            orders = OrderInfo.objects.filter(Q(order_id=keyword) |
                                              Q(skus__sku__name__contains=keyword))

        return orders


class OrdersViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        else:
            return OrderDetailSerializer

    def get_queryset(self):
        # 获取搜索关键字
        keyword = self.request.query_params.get('keyword')

        if not keyword:
            orders = OrderInfo.objects.all()
        else:
            orders = OrderInfo.objects.filter(Q(order_id=keyword) |
                                              Q(skus__sku__name__contains=keyword))

        return orders

    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        """
              修改订单状态:
              1. 校验订单是否有效
              2. 获取订单状态status并校验(status必传，status是否合法)
              3. 修改并保存订单的状态
              4. 返回应答
        """
        return self.update(request, pk)
