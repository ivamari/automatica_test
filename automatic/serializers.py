from rest_framework import serializers

from automatic.models import PointSale, Visit


class PointSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointSale
        fields = (
            'id',
            'name',
        )


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id',
                  'point_sale',
                  'worker',
                  'latitude',
                  'longitude',
                  'date_time')
