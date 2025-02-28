from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/save/', views.save_restaurant_details,
         name='save_restaurant_details'),
    path('api/restaurants/', views.get_restaurants, name='get_restaurants'),
    path("api/restaurants/<int:restaurant_id>/slots/", views.get_available_slots, name="get_available_slots"),
    path("api/restaurants/<int:restaurant_id>/reviews/", views.get_reviews, name="get_reviews"),
    path("api/restaurants/<int:restaurant_id>/menu/", views.get_menu, name="get_menu"),
]
