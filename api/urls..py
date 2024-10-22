from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Créer un router
router = DefaultRouter()
# Enregistrer le ViewSet avec le router
router.register(r'users', UserViewSet)

# Inclure les URLs du router
urlpatterns = [
    path('', include(router.urls)),
]