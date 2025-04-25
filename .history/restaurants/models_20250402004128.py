from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Restaurant(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=False)
    address = models.TextField(blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    cuisine = models.CharField(max_length=50, blank=False)
    lowest_price = models.FloatField(default=0.0)
    highest_price = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='restaurant_images', blank=False, null=True)
    rating = models.FloatField(default=0.0)  # Stores the average rating

    def get_average_rating(self):
        """Computes the average rating from reviews"""
        avg_rating = self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return avg_rating if avg_rating else 0.0

    def update_rating(self):
        """Updates the rating field"""
        self.rating = self.get_average_rating()
        self.save()

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=100, blank=False)  # User's display name
    rating = models.FloatField(default=0.0)
    comment = models.TextField(default="")

    def save(self, *args, **kwargs):
        """Override save to update restaurant rating"""
        super().save(*args, **kwargs)
        self.restaurant.update_rating()

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} ({self.rating})"


class RestaurantHour(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="hours")
    weekday = models.CharField(max_length=20, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    opening_time = models.TimeField(blank=False)
    closing_time = models.TimeField(blank=False)

    def __str__(self):
        return f"{self.restaurant.name} - {self.weekday}: {self.opening_time} to {self.closing_time}"

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return f"{self.restaurant.name} - {self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
    is_available = models.BooleanField(default=True)  # NEW

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.CharField(max_length=10, blank=False)
    capacity = models.IntegerField(blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="tables")

    def __str__(self):
        return f"Table {self.number} - {self.restaurant.name}"


class Slot(models.Model):
    time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="slots")
    customer_name = models.CharField(max_length=120, blank=True, null=True)  # NEW
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('booked', 'Booked'),
            ('pending', 'Pending')
        ],
        default='available'
    )

    def __str__(self):
        return f"{self.date} {self.time} - {self.table.restaurant.name}"


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE)
    table = models.ForeignKey("restaurants.Table", on_delete=models.CASCADE)
    slot = models.ForeignKey("restaurants.Slot", on_delete=models.CASCADE)
    date = models.DateField()
    number_of_guests = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Reservation {self.id} - {self.user.username}"


class SavedRestaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="saved_restaurants")
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE, related_name="saved_by_users")

    class Meta:
        unique_together = ("user", "restaurant")

    def __str__(self):
        return f"{self.user.username} saved {self.restaurant.name}"


class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="cuisine_images/")
    keyword = models.TextField(help_text="Keywords for searching cuisines")

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Review)
def update_restaurant_rating_on_delete(sender, instance, **kwargs):
    instance.restaurant.update_rating()