from api.serializers import DishesSerializer, ReviewsSerializer, ReservationSerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Dishes, Review, Reservation
from .pagination import TenItemsPagination, TwelveItemsPagination

class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    pagination_class = TenItemsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = TenItemsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dish']
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method.lower() == 'post' or self.request.method.lower() == 'get':
            return [permissions.AllowAny()]
        return super().get_permissions()


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    pagination_class = TenItemsPagination
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method.lower() == 'post' or self.request.method.lower() == 'get':
            return [permissions.AllowAny()]
        return super().get_permissions()