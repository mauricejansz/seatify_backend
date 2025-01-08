from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=False)
    address = models.TextField(blank=False)
    phone = models.CharField(max_length=15, blank=False)
    cuisine = models.CharField(max_length=50, blank=False)
    rating = models.FloatField(default=0.0)
    lowest_price = models.FloatField(default=0.0)
    highest_price = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='restaurant_images', blank=False, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="categories", blank=False)

    def __str__(self):
        return f"{self.restaurant} - {self.name}g"


class MenuItem(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items", blank=False)

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.CharField(max_length=10, blank=False)
    capacity = models.IntegerField(blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="tables", blank=False)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.number}"


class Slot(models.Model):
    time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="slots", blank=False)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + " " + self.time.strftime("%H:%M")
