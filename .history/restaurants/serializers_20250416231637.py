import base64
from rest_framework import serializers
from .models import Restaurant, Reservation, Review, SavedRestaurant, Cuisine, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name']


class RestaurantSerializer(serializers.ModelSerializer):
    image_data = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    menu_items = MenuItemSerializer(
        source="categories.menu_items", many=True, read_only=True)
    cuisine_name = serializers.CharField(source="cuisine.name", read_only=True)

    class Meta:
        model = Restaurant
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
            "menu_items"
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
        model = Reservation
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')  # Include user ID
    user_name = serializers.ReadOnlyField(
        source='user.username')  # Include username

    class Meta:
        model = Review
        fields = ["id", "user_id", "user_name",
                  "restaurant_id", "name", "rating", "comment"]


class SavedRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedRestaurant
        fields = ["id", "restaurant", "user"]


class CuisineSerializer(serializers.ModelSerializer):
    image_data = serializers.SerializerMethodField()

    class Meta:
        model = Cuisine
        fields = ["id", "name", "image_data", "keyword"]

    def get_image_data(self, obj):
        """Convert cuisine image to Base64"""
        if obj.image:
            with open(obj.image.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        return None
