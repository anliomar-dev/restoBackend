from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishesViewSet, ReviewViewSet
router = DefaultRouter()
router.register('dishes', DishesViewSet)
router.register('reviews', ReviewViewSet)
# router.register('reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]