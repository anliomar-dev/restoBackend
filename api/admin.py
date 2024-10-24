from django.contrib import admin

from api.models import Dishes, Review, Reservation


class DishesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'average']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['created', 'rating']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'time_slot', 'number_of_people']

admin.site.register(Dishes, DishesAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Reservation, ReservationAdmin)