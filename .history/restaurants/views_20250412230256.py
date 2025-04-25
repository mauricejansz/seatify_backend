from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .models import Restaurant, Category, MenuItem, Slot, Table, Reservation, Review, SavedRestaurant, Cuisine, EmailVerification
from django.contrib.auth.models import User
import json
import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RestaurantSerializer, ReservationSerializer, ReviewSerializer, SavedRestaurantSerializer, CuisineSerializer
from datetime import datetime


@login_required(login_url='accounts:login')
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})


@login_required(login_url='accounts:login')
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

        restaurant.name = data.get("restaurant-name", restaurant.name)
        restaurant.phone = data.get("phone", restaurant.phone)
        restaurant.address = data.get("address", restaurant.address)
        restaurant.description = data.get(
            "description", restaurant.description
        )
        restaurant.latitude = data.get("latitude", restaurant.latitude)
        restaurant.longitude = data.get("longitude", restaurant.longitude)
        restaurant.cuisine = data.get("cuisine", restaurant.cuisine)
        restaurant.save()

        deleted_categories = data.get("deleted_categories", [])
        Category.objects.filter(id__in=deleted_categories).delete()

        deleted_menu_items = data.get("deleted_menu_items", [])
        MenuItem.objects.filter(id__in=deleted_menu_items).delete()

        deleted_tables = data.get("deleted_tables", [])
        restaurant.tables.filter(id__in=deleted_tables).delete()

        deleted_slots = data.get("deleted_slots", [])
        Slot.objects.filter(id__in=deleted_slots).delete()

        new_categories = data.get("new_categories", [])
        for new_category in new_categories:
            Category.objects.create(
                restaurant=restaurant, name=new_category["name"]
            )

        updated_categories = data.get("updated_categories", [])
        for updated_category in updated_categories:
            category = get_object_or_404(Category, id=updated_category["id"])
            category.name = updated_category["name"]
            category.save()

        new_menu_items = data.get("new_menu_items", [])
        for new_item in new_menu_items:
            category = Category.objects.filter(
                name=new_item["category_name"], restaurant=restaurant
            ).first()
            if category:
                category.menu_items.create(
                    name=new_item["name"],
                    description=new_item["description"],
                    price=new_item["price"]
                )

        updated_menu_items = data.get("updated_menu_items", [])
        for updated_item in updated_menu_items:
            menu_item = get_object_or_404(MenuItem, id=updated_item["id"])
            menu_item.name = updated_item.get("name", menu_item.name)
            menu_item.description = updated_item.get(
                "description", menu_item.description
            )
            menu_item.price = updated_item.get("price", menu_item.price)
            menu_item.save()

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

        new_slots = data.get("new_slots", [])
        for new_slot in new_slots:
            table = Table.objects.filter(
                id=new_slot["table_id"], restaurant=restaurant
            ).first()
            if table:
                table.slots.create(
                    time=new_slot["time"],
                    date=new_slot["date"]
                )

        updated_slots = data.get("updated_slots", [])
        for updated_slot in updated_slots:
            slot = get_object_or_404(Slot, id=updated_slot["id"])
            slot.table = Table.objects.filter(
                id=updated_slot["table_id"], restaurant=restaurant).first()
            slot.time = updated_slot.get("time", slot.time)
            slot.date = updated_slot.get("date", slot.date)
            slot.save()

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_available_slots(request, restaurant_id):
    num_guests = request.GET.get("guests", None)
    date_str = request.GET.get("date", None)

    if num_guests is None or date_str is None:
        return Response({"error": "Please provide the number of guests and a date."}, status=400)

    try:
        num_guests = int(num_guests)
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "Invalid number of guests or date format."}, status=400)

    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    available_tables = restaurant.tables.filter(capacity__gte=num_guests)

    available_slots = Slot.objects.filter(
        table__in=available_tables,
        status="available",
        date=date_obj
    ).order_by("time")

    slots_data = [
        {
            "id": slot.id,
            "table": slot.table.number,
            "capacity": slot.table.capacity,
            "date": slot.date.strftime("%Y-%m-%d"),
            "time": slot.time.strftime("%H:%M"),
            "status": slot.status
        }
        for slot in available_slots
    ]

    return Response(slots_data, status=200)


@api_view(["GET"])
def get_reviews(request, restaurant_id):
    """Retrieve all reviews for a restaurant, ordered by latest."""
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all().order_by("-id")

    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(["GET"])
def get_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    categories = restaurant.categories.all()

    menu_data = []
    for category in categories:
        menu_items = category.menu_items.filter(is_available=True)
        items_data = [
            {
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "price": str(item.price)
            }
            for item in menu_items
        ]

        menu_data.append({
            "category": category.name,
            "items": items_data
        })

    return Response(menu_data, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_reservation(request):
    user = request.user
    data = request.data

    restaurant_id = data.get("restaurant_id")
    slot_id = data.get("slot_id")
    number_of_guests = data.get("number_of_guests")
    comments = data.get("comments", "")

    if not all([restaurant_id, slot_id, number_of_guests]):
        return Response({"error": "Missing required fields"}, status=400)

    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    slot = get_object_or_404(Slot, id=slot_id)
    table = slot.table
    date = slot.date

    if slot.status != "available":
        return Response({"error": "Selected slot is not available"}, status=400)

    reservation = Reservation.objects.create(
        user=user,
        restaurant=restaurant,
        table=table,
        slot=slot,
        date=date,
        number_of_guests=number_of_guests,
        comments=comments,
        status="confirmed",
        payment_status="paid",
    )

    slot.status = "reserved"
    slot.save()

    return Response(ReservationSerializer(reservation).data, status=201)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_review(request, restaurant_id):
    """
    Endpoint to allow authenticated users to add a review to a restaurant.
    """
    user = request.user
    restaurant = Restaurant.objects.filter(id=restaurant_id).first()

    if not restaurant:
        return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

    rating = request.data.get("rating")
    if rating is None or not (0.0 <= float(rating) <= 5.0):
        return Response({"error": "Invalid rating. Must be between 0 and 5."}, status=400)

    comment = request.data.get("comment", "")

    if Review.objects.filter(user=user, restaurant=restaurant).exists():
        return Response({"error": "You have already reviewed this restaurant."}, status=400)

    review = Review.objects.create(
        restaurant=restaurant,
        user=user,
        name=user.username,
        rating=float(rating),
        comment=comment
    )

    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    """
    Endpoint to allow users to delete their own reviews.
    """
    user = request.user
    review = Review.objects.filter(id=review_id).first()

    if not review:
        return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

    if review.user != user:
        return Response({"error": "You can only delete your own reviews."}, status=status.HTTP_403_FORBIDDEN)

    review.delete()
    return Response({"message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def toggle_saved_restaurant(request, restaurant_id):
    user = request.user
    restaurant = Restaurant.objects.get(id=restaurant_id)

    saved_entry, created = SavedRestaurant.objects.get_or_create(
        user=user, restaurant=restaurant
    )

    if not created:
        saved_entry.delete()
        return Response({"message": "Restaurant removed from saved list."}, status=status.HTTP_200_OK)

    return Response({"message": "Restaurant added to saved list."}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_saved_restaurants(request):
    user = request.user
    saved_restaurants = SavedRestaurant.objects.filter(user=user)
    serializer = SavedRestaurantSerializer(saved_restaurants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_cuisines(request):
    cuisines = Cuisine.objects.all()
    serializer = CuisineSerializer(
        cuisines, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_recent_bookings(request):
    user = request.user

    restaurant_ids = (
        Reservation.objects
        .filter(user=user)
        .order_by('-date')
        .values_list("restaurant_id", flat=True)
        .distinct()[:5]
    )

    recent_restaurants = Restaurant.objects.filter(id__in=restaurant_ids)

    serializer = RestaurantSerializer(recent_restaurants, many=True)
    return Response(serializer.data, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_saved_restaurant_details(request):
    user = request.user

    saved_restaurants = SavedRestaurant.objects.filter(user=user)

    restaurant_ids = saved_restaurants.values_list("restaurant_id", flat=True)

    restaurants = Restaurant.objects.filter(id__in=restaurant_ids)

    serializer = RestaurantSerializer(restaurants, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_saved_status(request, restaurant_id):
    """
    Check if a restaurant is saved by the current user.
    """
    user = request.user
    is_saved = SavedRestaurant.objects.filter(
        user=user, restaurant_id=restaurant_id).exists()
    return Response({"saved": is_saved}, status=200)


@api_view(["POST"])
def send_verification_email(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    code = str(random.randint(100000, 999999))

    # Save or update verification record
    EmailVerification.objects.update_or_create(
        user=user,
        defaults={"code": code, "is_verified": False}
    )

    # Render email HTML template
    subject = "Verify your email - Seatify"
    html_message = render_to_string(
        "emails/verify_email.html", {"user": user, "code": code})
    email_message = EmailMessage(subject, html_message, to=[email])
    email_message.content_subtype = "html"
    email_message.send()

    return Response({"message": "Verification email sent"}, status=200)


@api_view(["POST"])
def verify_email_code(request):
    email = request.data.get("email")
    code = request.data.get("code")
    user = get_object_or_404(User, email=email)

    try:
        record = EmailVerification.objects.get(user=user)
        if record.code == code:
            record.is_verified = True
            record.save()
            return Response({"message": "Email verified successfully"}, status=200)
        else:
            return Response({"error": "Invalid verification code"}, status=400)
    except EmailVerification.DoesNotExist:
        return Response({"error": "Verification record not found"}, status=404)
