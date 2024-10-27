from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.serializers import DishesSerializer, ReviewsSerializer, ReservationSerializer
from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Dishes, Review, Reservation
from .pagination import TenItemsPagination, TwelveItemsPagination

class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    pagination_class = TenItemsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method.lower() == 'get':
            return [permissions.AllowAny()]
        return super().get_permissions()

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
