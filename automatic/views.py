from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import PointSale, Visit
from .authentication import PhoneAuthentication
from .serializers import PointSaleSerializer, VisitSerializer


@extend_schema_view(
    get=extend_schema(summary='Список торговых точек', tags=['Торговые точки']),
)
class PointSaleListView(APIView):
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        worker = request.user
        point_sales = PointSale.objects.filter(worker=worker)
        if not point_sales.exists():
            return Response(
                {'error': 'No point of sale found for the worker'},
                status=status.HTTP_404_NOT_FOUND)

        serializer = PointSaleSerializer(point_sales, many=True)
        return Response(serializer.data)


@extend_schema_view(
    post=extend_schema(summary='Создать посещение', tags=['Посещения']),
)
class VisitCreateView(APIView):
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        worker = request.user
        point_sale_id = request.data.get('point_sale')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if not all([point_sale_id, latitude, longitude]):
            return Response({'error': 'Отсутствуют обязательные поля'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            point_sale = PointSale.objects.get(pk=point_sale_id)
        except PointSale.DoesNotExist:
            return Response({'error': 'Торговая точка не найдена'},
                            status=status.HTTP_404_NOT_FOUND)

        if point_sale.worker != worker:
            return Response(
                {'error': 'Работник не связан с этой торговой точкой'},
                status=status.HTTP_403_FORBIDDEN)

        visit = Visit.objects.create(
            point_sale=point_sale,
            worker=worker,
            latitude=latitude,
            longitude=longitude
        )

        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
