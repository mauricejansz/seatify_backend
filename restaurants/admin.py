from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Restaurant)
admin.site.register(models.Category)
admin.site.register(models.MenuItem)
admin.site.register(models.Table)
admin.site.register(models.Slot)
admin.site.register(models.SavedRestaurant)
admin.site.register(models.RestaurantHour)
admin.site.register(models.Review)
admin.site.register(models.Reservation)
admin.site.register(models.Cuisine)


