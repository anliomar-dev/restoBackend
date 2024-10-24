from api.serializers import DishesSerializer, ReviewsSerializer, ReservationSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Dishes, Review, Reservation
from .pagination import TenItemsPagination, TwelveItemsPagination


class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    pagination_class = TenItemsPagination  # Pagination de 10 éléments par page
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']