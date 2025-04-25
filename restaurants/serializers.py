import base64
from rest_framework import serializers
from . import models


class CuisineSerializer(serializers.ModelSerializer):
    image_data = serializers.SerializerMethodField()

    class Meta:
        model = models.Cuisine
        fields = ["id", "name", "image_data", "keyword"]

    def get_image_data(self, obj):
        if obj.image:
            with open(obj.image.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        return None


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ["id", "name", "description", "price"]


class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(source="menu_items", many=True, read_only=True)
    category = serializers.CharField(source="name")

    class Meta:
        model = models.Category
        fields = ["category", "items"]


class RestaurantSerializer(serializers.ModelSerializer):
    image_data = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    menu_categories = MenuCategorySerializer(
        source="categories", many=True, read_only=True)
    cuisine = CuisineSerializer(read_only=True)

    class Meta:
        model = models.Restaurant
        fields = [
            "id",
            "name",
            "description",
            "address",
            "phone",
            "cuisine",
            "rating",
            "lowest_price",
            "highest_price",
            "is_published",
            "latitude",
            "longitude",
            "image_data",
            "review_count",
            "menu_categories"
        ]

    def get_image_data(self, obj):
        if obj.image:
            with open(obj.image.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        return None

    def get_review_count(self, obj):
        """Returns the total number of reviews for the restaurant"""
        return obj.reviews.all().count()


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    user_name = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = models.Review
        fields = ["id", "user_id", "user_name",
                  "restaurant_id", "name", "rating", "comment"]


class SavedRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavedRestaurant
        fields = ["id", "restaurant", "user"]
        

class ReservationListSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    slot_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Reservation
        fields = [
            "id", "restaurant", "date", "slot_time",
            "number_of_guests", "status", "payment_status"
        ]

    def get_slot_time(self, obj):
        return obj.slot.time.strftime("%H:%M") if obj.slot else None
