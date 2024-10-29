from django.core.exceptions import ValidationError
from django.db.models import Max
from django.test import Client, TestCase

from .models import Dishes, Review, Reservation

# Create your tests here.

class TestDishes(TestCase):
    def setUp(self):
        dish_one = Dishes.objects.create(
            name='Dish 1', price=10.5,
            description='desription for Dish 1', ingredients="ingredient 1.1, ingredient 1.2"
        )
        dish_two = Dishes.objects.create(
            name='Dish 2', price=10000.23,
            description='desription for Dish 2', ingredients="ingredient 2.1, ingredient 2.2"
        )

        dish_three = Dishes.objects.create(
            name='Dish 3', price=9,
            description='desription for Dish 3', ingredients="ingredient 3.1, ingredient 3.2", average=10
        )

    def test_dish_valid(self):
        dish = Dishes.objects.get(name='Dish 1')
        is_dish_valid = False
        try:
            dish.full_clean()  # validate all fields
            is_dish_valid = True  # if there is no exception
        except ValidationError:
            is_dish_valid = False  # if there is an exception

       # check if all field ar vaid
        self.assertEqual(is_dish_valid, True)

    def test_dish_price_not_valid(self):
        dish = Dishes.objects.get(name='Dish 2')

        # raise exception if the number of digit of the price is greather than 5 or
        # decimal places is more than 2
        with self.assertRaises(ValidationError):
            dish.full_clean(['price'])

    def test_average_initial_value(self):
        new_dish = Dishes.objects.create(
            name='Dish 4', price=25.0,
            description='description for Dish 4', ingredients="ingredient 4.1, ingredient 4.2"
        )
        other_dish = Dishes.objects.get(name='Dish 3')
        # check if initial value of average is zero
        self.assertEqual(new_dish.average, 0)
        self.assertNotEqual(other_dish.average, 0)

