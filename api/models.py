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

    reservation_date = models.DateField()
    time_slot = models.TimeField()
    number_of_people = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # Valeur par défaut

    def __str__(self):
        return f"Reservation for {self.number_of_people} people on {self.reservation_date} at {self.time_slot}"
