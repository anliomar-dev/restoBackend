from django.template.context_processors import request
from rest_framework import serializers, permissions
from api.models import Dishes, Review, Reservation

class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


