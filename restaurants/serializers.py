import base64
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    image_data = serializers.SerializerMethodField()

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
            "image_data"  # This will return the image as base64
        ]

    def get_image_data(self, obj):
        if obj.image:
            with open(obj.image.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        return None