from restaurants.models import Cuisine, Restaurant, Category, MenuItem, Review
from accounts.models import User
from django.contrib.auth.hashers import make_password
from datetime import date

# Create Users
# Restaurant Managers
giovanni_manager, _ = User.objects.get_or_create(
    username="giovanni_manager",
    defaults={
        "email": "manager@giovannis.lk",
        "password": make_password("manager123"),
        "first_name": "Marco",
        "last_name": "Rossi",
        "role": "manager",
        "phone_number": "+94771234567",
        "date_of_birth": date(1985, 5, 15),
        "is_verified": True
    }
)

culture_manager, _ = User.objects.get_or_create(
    username="culture_manager",
    defaults={
        "email": "manager@culturecolombo.lk",
        "password": make_password("manager123"),
        "first_name": "Nimal",
        "last_name": "Perera",
        "role": "manager",
        "phone_number": "+94764567890",
        "date_of_birth": date(1980, 8, 22),
        "is_verified": True
    }
)

monsoon_manager, _ = User.objects.get_or_create(
    username="monsoon_manager",
    defaults={
        "email": "manager@monsooncolombo.lk",
        "password": make_password("manager123"),
        "first_name": "Priya",
        "last_name": "Fernando",
        "role": "manager",
        "phone_number": "+94772227389",
        "date_of_birth": date(1988, 3, 10),
        "is_verified": True
    }
)

# Regular Users
user1, _ = User.objects.get_or_create(
    username="john_doe",
    defaults={
        "email": "john.doe@example.com",
        "password": make_password("user123"),
        "first_name": "John",
        "last_name": "Doe",
        "role": "user",
        "phone_number": "+94771234568",
        "date_of_birth": date(1990, 1, 1),
        "is_verified": True
    }
)

user2, _ = User.objects.get_or_create(
    username="sarah_smith",
    defaults={
        "email": "sarah.smith@example.com",
        "password": make_password("user123"),
        "first_name": "Sarah",
        "last_name": "Smith",
        "role": "user",
        "phone_number": "+94771234569",
        "date_of_birth": date(1992, 2, 2),
        "is_verified": True
    }
)

user3, _ = User.objects.get_or_create(
    username="mike_wilson",
    defaults={
        "email": "mike.wilson@example.com",
        "password": make_password("user123"),
        "first_name": "Mike",
        "last_name": "Wilson",
        "role": "user",
        "phone_number": "+94771234570",
        "date_of_birth": date(1988, 3, 3),
        "is_verified": True
    }
)

user4, _ = User.objects.get_or_create(
    username="lisa_jones",
    defaults={
        "email": "lisa.jones@example.com",
        "password": make_password("user123"),
        "first_name": "Lisa",
        "last_name": "Jones",
        "role": "user",
        "phone_number": "+94771234571",
        "date_of_birth": date(1995, 4, 4),
        "is_verified": True
    }
)

user5, _ = User.objects.get_or_create(
    username="david_brown",
    defaults={
        "email": "david.brown@example.com",
        "password": make_password("user123"),
        "first_name": "David",
        "last_name": "Brown",
        "role": "user",
        "phone_number": "+94771234572",
        "date_of_birth": date(1993, 5, 5),
        "is_verified": True
    }
)

# Create Cuisines
italian, _ = Cuisine.objects.get_or_create(
    name="Italian",
    defaults={
        "image": "cuisine_images/italian.jpg",
        "keyword": "pizza, pasta, Italian, Colombo"
    }
)

sri_lankan, _ = Cuisine.objects.get_or_create(
    name="Sri Lankan",
    defaults={
        "image": "cuisine_images/srilankan.jpg",
        "keyword": "Sri Lankan, rice and curry, local food"
    }
)

international, _ = Cuisine.objects.get_or_create(
    name="International",
    defaults={
        "image": "cuisine_images/international.jpg",
        "keyword": "buffet, international, fusion, cuban, latin, cocktails, beach, thai, vietnamese, asian fusion"
    }
)

grill_seafood, _ = Cuisine.objects.get_or_create(
    name="Grill & Seafood",
    defaults={
        "image": "cuisine_images/grillseafood.jpg",
        "keyword": "grill, barbecue, beach restaurant, seafood, buffet, luxury dining"
    }
)

fine_dining, _ = Cuisine.objects.get_or_create(
    name="Fine Dining",
    defaults={
        "image": "cuisine_images/finedining.jpg",
        "keyword": "fine dining, rooftop, luxury"
    }
)

buffet, _ = Cuisine.objects.get_or_create(
    name="Buffet",
    defaults={
        "image": "cuisine_images/buffet.jpg",
        "keyword": "international buffet, graze, hilton"
    }
)

german, _ = Cuisine.objects.get_or_create(
    name="German",
    defaults={
        "image": "cuisine_images/german.jpg",
        "keyword": "german, beer, sausages, pork knuckle"
    }
)

# Create Restaurants with their unique menus
# 1. Giovannis (Italian)
giovannis = Restaurant.objects.create(
    name="Giovannis",
    description="Authentic Italian cuisine in the heart of Colombo",
    address="Colpetty, Colombo, Sri Lanka",
    phone="+94 77 123 4567",
    email="info@giovannis.lk",
    website="https://giovannis.lk",
    cuisine=italian,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9022,
    longitude=79.8613,
    image="media/restaurant_images/Giovannis.jpg",
    user=giovanni_manager
)

# Giovannis Menu
antipasti = Category.objects.create(name="Antipasti", restaurant=giovannis)
pasta = Category.objects.create(name="Pasta", restaurant=giovannis)
pizza = Category.objects.create(name="Pizza", restaurant=giovannis)
dolci = Category.objects.create(name="Dolci", restaurant=giovannis)
vino = Category.objects.create(name="Vino", restaurant=giovannis)

MenuItem.objects.create(
    name="Bruschetta al Pomodoro",
    description="Toasted bread with fresh tomatoes, garlic, and basil",
    price=1200,
    category=antipasti,
    is_available=True
)
MenuItem.objects.create(
    name="Carpaccio di Manzo",
    description="Thinly sliced raw beef with arugula and parmesan",
    price=1800,
    category=antipasti,
    is_available=True
)
MenuItem.objects.create(
    name="Spaghetti Carbonara",
    description="Classic pasta with eggs, cheese, pancetta, and black pepper",
    price=2200,
    category=pasta,
    is_available=True
)
MenuItem.objects.create(
    name="Fettuccine Alfredo",
    description="Fresh fettuccine with creamy parmesan sauce",
    price=2400,
    category=pasta,
    is_available=True
)
MenuItem.objects.create(
    name="Margherita Pizza",
    description="Classic pizza with tomato sauce, mozzarella, and basil",
    price=2000,
    category=pizza,
    is_available=True
)
MenuItem.objects.create(
    name="Quattro Formaggi",
    description="Four cheese pizza with mozzarella, gorgonzola, parmesan, and ricotta",
    price=2500,
    category=pizza,
    is_available=True
)
MenuItem.objects.create(
    name="Tiramisu",
    description="Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream",
    price=1200,
    category=dolci,
    is_available=True
)
MenuItem.objects.create(
    name="Panna Cotta",
    description="Creamy Italian dessert with berry compote",
    price=1100,
    category=dolci,
    is_available=True
)
MenuItem.objects.create(
    name="Chianti Classico",
    description="2018 vintage, Tuscany",
    price=3500,
    category=vino,
    is_available=True
)

# 2. Culture Colombo (Sri Lankan)
culture_colombo = Restaurant.objects.create(
    name="Culture Colombo",
    description="Experience authentic Sri Lankan cuisine in a modern setting",
    address="Bauddhaloka Mawatha, Colombo 07, Sri Lanka",
    phone="+94 76 456 7890",
    email="reservations@culturecolombo.lk",
    website="https://culturecolombo.lk",
    cuisine=sri_lankan,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9147,
    longitude=79.8665,
    image="media/restaurant_images/CultureColombo.jpg",
    user=culture_manager
)

# Culture Colombo Menu
rice = Category.objects.create(name="Rice & Curry", restaurant=culture_colombo)
hoppers = Category.objects.create(
    name="Hoppers & String Hoppers", restaurant=culture_colombo)
seafood = Category.objects.create(
    name="Seafood Specialties", restaurant=culture_colombo)
desserts = Category.objects.create(
    name="Traditional Desserts", restaurant=culture_colombo)
beverages = Category.objects.create(
    name="Traditional Beverages", restaurant=culture_colombo)

MenuItem.objects.create(
    name="Traditional Rice & Curry",
    description="White rice with 5 curries and sambol",
    price=1500,
    category=rice,
    is_available=True
)
MenuItem.objects.create(
    name="Kottu Roti",
    description="Chopped roti with vegetables, egg, and choice of meat",
    price=1800,
    category=rice,
    is_available=True
)
MenuItem.objects.create(
    name="Egg Hoppers",
    description="Traditional Sri Lankan hoppers with egg",
    price=800,
    category=hoppers,
    is_available=True
)
MenuItem.objects.create(
    name="String Hoppers",
    description="Steamed rice flour noodles with coconut sambol",
    price=900,
    category=hoppers,
    is_available=True
)
MenuItem.objects.create(
    name="Devilled Prawns",
    description="Spicy stir-fried prawns with onions and peppers",
    price=2800,
    category=seafood,
    is_available=True
)
MenuItem.objects.create(
    name="Ambul Thiyal",
    description="Traditional sour fish curry with goraka",
    price=2500,
    category=seafood,
    is_available=True
)
MenuItem.objects.create(
    name="Watalappan",
    description="Traditional Sri Lankan coconut custard pudding",
    price=900,
    category=desserts,
    is_available=True
)
MenuItem.objects.create(
    name="Kiri Pani",
    description="Traditional milk toffee",
    price=800,
    category=desserts,
    is_available=True
)
MenuItem.objects.create(
    name="King Coconut",
    description="Fresh thambili",
    price=400,
    category=beverages,
    is_available=True
)

# 3. Monsoon Colombo (International)
monsoon = Restaurant.objects.create(
    name="Monsoon Colombo",
    description="Fusion cuisine with Asian and international influences",
    address="50/2 Park Street, Colombo 00200, Sri Lanka",
    phone="+94 11 230 2449",
    email="reservations@monsooncolombo.com",
    website="https://www.monsooncolombo.com",
    cuisine=international,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9219,
    longitude=79.8567,
    image="media/restaurant_images/2025-01-18.jpg",
    user=monsoon_manager
)

# Monsoon Colombo Menu
starters = Category.objects.create(name="Starters", restaurant=monsoon)
mains = Category.objects.create(name="Main Courses", restaurant=monsoon)
sides = Category.objects.create(name="Sides", restaurant=monsoon)
desserts = Category.objects.create(name="Desserts", restaurant=monsoon)
cocktails = Category.objects.create(
    name="Signature Cocktails", restaurant=monsoon)

MenuItem.objects.create(
    name="Crispy Calamari",
    description="Fried calamari with sweet chili sauce",
    price=1800,
    category=starters,
    is_available=True
)
MenuItem.objects.create(
    name="Duck Spring Rolls",
    description="Crispy spring rolls with hoisin sauce",
    price=2000,
    category=starters,
    is_available=True
)
MenuItem.objects.create(
    name="Beef Rendang",
    description="Slow-cooked beef in rich coconut curry",
    price=2800,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Pad Thai",
    description="Stir-fried rice noodles with prawns and peanuts",
    price=2200,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Stir-fried Vegetables",
    description="Seasonal vegetables in oyster sauce",
    price=1200,
    category=sides,
    is_available=True
)
MenuItem.objects.create(
    name="Mango Sticky Rice",
    description="Sweet sticky rice with fresh mango",
    price=1100,
    category=desserts,
    is_available=True
)
MenuItem.objects.create(
    name="Monsoon Breeze",
    description="Signature cocktail with rum, coconut, and tropical fruits",
    price=1500,
    category=cocktails,
    is_available=True
)

# Add Reviews
# Giovannis Reviews
Review.objects.create(
    restaurant=giovannis,
    user=user1,
    name="John Doe",
    rating=4.5,
    comment="Amazing Italian food! The pasta was perfect and the service was excellent."
)

Review.objects.create(
    restaurant=giovannis,
    user=user2,
    name="Sarah Smith",
    rating=5.0,
    comment="Best pizza in Colombo! The atmosphere is lovely and the staff is very friendly."
)

Review.objects.create(
    restaurant=giovannis,
    user=user3,
    name="Mike Wilson",
    rating=4.0,
    comment="Great food but a bit pricey. The wine selection is impressive."
)

# Culture Colombo Reviews
Review.objects.create(
    restaurant=culture_colombo,
    user=user4,
    name="Lisa Jones",
    rating=5.0,
    comment="Authentic Sri Lankan cuisine at its best! The hoppers were amazing."
)

Review.objects.create(
    restaurant=culture_colombo,
    user=user5,
    name="David Brown",
    rating=4.5,
    comment="Loved the traditional rice and curry. The service was excellent."
)

Review.objects.create(
    restaurant=culture_colombo,
    user=user1,
    name="John Doe",
    rating=4.0,
    comment="Great place to experience local cuisine. The seafood dishes are outstanding."
)

# Monsoon Colombo Reviews
Review.objects.create(
    restaurant=monsoon,
    user=user2,
    name="Sarah Smith",
    rating=4.5,
    comment="Beautiful fusion cuisine. The cocktails are creative and delicious."
)

Review.objects.create(
    restaurant=monsoon,
    user=user3,
    name="Mike Wilson",
    rating=5.0,
    comment="One of my favorite restaurants in Colombo. The beef rendang is a must-try!"
)

Review.objects.create(
    restaurant=monsoon,
    user=user4,
    name="Lisa Jones",
    rating=4.0,
    comment="Great atmosphere and food. The service could be a bit faster though."
)
