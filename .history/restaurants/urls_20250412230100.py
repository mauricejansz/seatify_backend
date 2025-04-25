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
    path("api/restaurants/reservations/", views.create_reservation, name="create_reservation"),
    path("api/restaurants/<int:restaurant_id>/create_review/", views.create_review, name="create_review"),
    path("api/restaurants/delete_review/<int:review_id>/", views.delete_review, name="delete_review"),
    path("api/restaurants/saved/", views.get_saved_restaurants, name="get_saved_restaurants"),
    path("api/restaurants/saved/details/", views.get_saved_restaurant_details, name="get_saved_restaurant_details"),
    path("api/restaurants/saved/<int:restaurant_id>/", views.toggle_saved_restaurant, name="toggle_saved_restaurant"),
    path("api/restaurants/cuisines/", views.get_cuisines, name="get_cuisines"),
    path("api/restaurants/recent_bookings/", views.get_recent_bookings, name="get_recent_bookings"),
    path("api/restaurants/recent_bookings/", views.get_recent_bookings, name="get_recent_bookings"),
    path("api/restaurants/saved/<int:restaurant_id>/status/", views.check_saved_status, name="check_saved_status"),
    path("/api/verify_email/", views.check_saved_status, name="check_saved_status"),
]
