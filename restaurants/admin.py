from django.contrib import admin
from .models import Restaurant, Category, Table, Slot, MenuItem, SavedRestaurant, RestaurantHour, Review
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Slot)
admin.site.register(SavedRestaurant)
admin.site.register(RestaurantHour)
admin.site.register(Review)

