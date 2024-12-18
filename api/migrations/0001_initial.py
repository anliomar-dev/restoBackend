# Generated by Django 5.1.2 on 2024-10-24 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.CharField(choices=[('starter', 'Starter'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='starter', max_length=10)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('average', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('number_of_people', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'), ('completed', 'Completed'), ('no_show', 'No-Show')], default='pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.dishes')),
            ],
        ),
    ]
