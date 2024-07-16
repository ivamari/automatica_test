from django.urls import path
from .views import PointSaleListView, VisitCreateView

urlpatterns = [
    path('point-sales/', PointSaleListView.as_view(), name='point-sale-list'),
    path('visits/', VisitCreateView.as_view(), name='visit-create')
]
