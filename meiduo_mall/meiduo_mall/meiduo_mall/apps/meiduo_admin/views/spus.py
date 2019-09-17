# GET /meiduo_admin/goods/simple/
from requests import Response
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ViewSet, GenericViewSet, ReadOnlyModelViewSet

from goods.models import SPU, SPUSpecification
from meiduo_admin.serializer.spus import SPUSimpleSerializer, SPUSpecSerializer


class SPUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SPUSimpleSerializer
    queryset = SPU.objects.all()
    pagination_class = None

# GET meiduo_admin/goods/(?P<pk>\d+)/specs/
class SPUSpecView(ListAPIView):
    permission_classes = [IsAdminUser]

    # 指定序列化器类
    serializer_class = SPUSpecSerializer
    pagination_class = None

    def get_queryset(self):
        """返回视图所使用的查询集"""
        # 获取pk
        pk = self.kwargs['pk']
        return SPUSpecification.objects.filter(spu_id=pk)

    # 注：关闭分页


# GET meiduo_admin/goods/(?P<pk>\d+)/specs/
# class SPUSpecView(ReadOnlyModelViewSet):
#     permission_classes = [IsAdminUser]
#     serializer_class = SPUSpecSerializer
#     lookup_value_regex = '/d+'
#     pagination_class = None
#

    # def get(self, request, pk):
    #     """
    #            获取spu规格选项数据:
    #            1. 根据pk获取spu specs数据
    #            2. 将spu数据序列化并返回
    #            """
    #     # 1. 根据pk获取spu specs数据
    #     specs = SPUSpecification.objects.filter(spu_id=pk)
    #     # 2. 将spu数据序列化并返回
    #     serializer = SPUSpecSerializer(specs, many=True)
    #     return Response(serializer.data)

