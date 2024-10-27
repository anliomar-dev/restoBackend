from datetime import datetime, timedelta
from django.db import models

# Create your models here.

class Dishes(models.Model):
    CATEGORY_CHOICES = [
        ("starter", "Starter"),
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="starter")
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
        ("no_show", "No-Show"),
    ]
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    reservation_date = models.DateField()
    time_slot = models.TimeField()
    number_of_people = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # Valeur par défaut

    def __str__(self):
        return f"Reservation for {self.number_of_people} people on {self.reservation_date} at {self.time_slot}"

    def save(self, *args, **kwargs):
        if self.number_of_people < 1:
            self.number_of_people = 1
        return super().save(*args, **kwargs)

    def is_reservation_date_valid(self):
        """ check if reservation date is valid """
        return self.reservation_date >= datetime.date.today()

    def is_time_slot_valid(self):
        """Check if the time is at least 30 minutes from now."""
        now = datetime.now()
        # get actual time and add 30 minutes
        min_time = (now + datetime.timedelta(minutes=30)).time()
        reservation_time = self.time_slot
        return reservation_time >= min_time
