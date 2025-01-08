from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Restaurant, Category, MenuItem, Slot, Table

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    categories = restaurant.categories.all()
    tables = restaurant.tables.all()
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'categories': categories,
        'tables': tables,
    })

@csrf_exempt
def save_restaurant_details(request, restaurant_id):
    if request.method == "POST":
        data = json.loads(request.body)
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)

        # Update restaurant fields
        restaurant.name = data.get("restaurant-name", restaurant.name)
        restaurant.phone = data.get("phone", restaurant.phone)
        restaurant.address = data.get("address", restaurant.address)
        restaurant.description = data.get("description", restaurant.description)
        restaurant.latitude = data.get("latitude", restaurant.latitude)
        restaurant.longitude = data.get("longitude", restaurant.longitude)
        restaurant.cuisine = data.get("cuisine", restaurant.cuisine)
        restaurant.save()

        # Handle deleted categories
        deleted_categories = data.get("deleted_categories", [])
        Category.objects.filter(id__in=deleted_categories).delete()

        deleted_menu_items = data.get("deleted_menu_items", [])
        MenuItem.objects.filter(id__in=deleted_menu_items).delete()

        deleted_tables = data.get("deleted_tables", [])
        restaurant.tables.filter(id__in=deleted_tables).delete()

        deleted_slots = data.get("deleted_slots", [])
        Slot.objects.filter(id__in=deleted_slots).delete()

        # Handle new categories
        new_categories = data.get("new_categories", [])
        for new_category in new_categories:
            Category.objects.create(restaurant=restaurant, name=new_category["name"])

        # Handle updated categories
        updated_categories = data.get("updated_categories", [])
        for updated_category in updated_categories:
            category = get_object_or_404(Category, id=updated_category["id"])
            category.name = updated_category["name"]
            category.save()

        # Handle new menu items
        new_menu_items = data.get("new_menu_items", [])
        for new_item in new_menu_items:
            category = Category.objects.filter(name=new_item["category_name"], restaurant=restaurant).first()
            if category:
                category.menu_items.create(
                    name=new_item["name"],
                    description=new_item["description"],
                    price=new_item["price"]
                )

        # Handle updated menu items
        updated_menu_items = data.get("updated_menu_items", [])
        for updated_item in updated_menu_items:
            menu_item = get_object_or_404(MenuItem, id=updated_item["id"])
            menu_item.name = updated_item.get("name", menu_item.name)
            menu_item.description = updated_item.get("description", menu_item.description)
            menu_item.price = updated_item.get("price", menu_item.price)
            menu_item.save()

        # Handle new tables
        new_tables = data.get("new_tables", [])
        for new_table in new_tables:
            restaurant.tables.create(
                number=new_table["number"],
                capacity=new_table["capacity"]
            )

        updated_tables = data.get("updated_tables", [])
        for updated_table in updated_tables:
            table = restaurant.tables.filter(id=updated_table["id"]).first()
            if table:
                table.number = updated_table["number"]
                table.capacity = updated_table["capacity"]
                table.save()

        # Handle new slots
        new_slots = data.get("new_slots", [])
        for new_slot in new_slots:
            table = Table.objects.filter(id=new_slot["table_id"], restaurant=restaurant).first()
            if table:
                table.slots.create(
                    time=new_slot["time"],
                    date=new_slot["date"]
                )

        updated_slots = data.get("updated_slots", [])
        for updated_slot in updated_slots:
            slot = get_object_or_404(Slot, id=updated_slot["id"])
            slot.table = Table.objects.filter(id=updated_slot["table_id"], restaurant=restaurant).first()
            slot.time = updated_slot.get("time", slot.time)
            slot.date = updated_slot.get("date", slot.date)
            slot.save()

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)