from django.contrib import admin
from .models import Restaurant, Category, Table, Slot, MenuItem
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Slot)

