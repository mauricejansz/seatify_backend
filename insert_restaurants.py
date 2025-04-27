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
    username="ted_mosby",
    defaults={
        "email": "ted.mosby@gmail.com",
        "password": make_password("user123"),
        "first_name": "Ted",
        "last_name": "Mosby",
        "role": "user",
        "phone_number": "+94771234568",
        "date_of_birth": date(1990, 1, 1),
        "is_verified": True
    }
)

user2, _ = User.objects.get_or_create(
    username="marshal_eriksen",
    defaults={
        "email": "marshal.eriksen@gmail.com",
        "password": make_password("user123"),
        "first_name": "Marshal",
        "last_name": "Eriksen",
        "role": "user",
        "phone_number": "+94771234569",
        "date_of_birth": date(1992, 2, 2),
        "is_verified": True
    }
)

user3, _ = User.objects.get_or_create(
    username="lily_aldrin",
    defaults={
        "email": "lily.aldrin@gmail.com",
        "password": make_password("user123"),
        "first_name": "Lily",
        "last_name": "Aldrin",
        "role": "user",
        "phone_number": "+94771234570",
        "date_of_birth": date(1988, 3, 3),
        "is_verified": True
    }
)

user4, _ = User.objects.get_or_create(
    username="barney_stinson",
    defaults={
        "email": "barney_stinson@gmail.com",
        "password": make_password("user123"),
        "first_name": "Barney",
        "last_name": "Stinson",
        "role": "user",
        "phone_number": "+94771234571",
        "date_of_birth": date(1995, 4, 4),
        "is_verified": True
    }
)

user5, _ = User.objects.get_or_create(
    username="robin_scherbatsky",
    defaults={
        "email": "robin_scherbatsky@gmail.com",
        "password": make_password("user123"),
        "first_name": "Robin",
        "last_name": "Scherbatsky",
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
    address="145 Thimbirigasyaya Rd, Colombo 00500",
    phone="+94 77 123 4567",
    email="info@giovannis.lk",
    website="https://giovannis.lk",
    cuisine=italian,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.891540128732606,
    longitude=79.86805530225179,
    image="media/restaurant_images/giovannis.jpg",
    user=giovanni_manager
)

# Giovannis Menu
starter = Category.objects.create(name="Starters", restaurant=giovannis)
pasta = Category.objects.create(name="Pasta", restaurant=giovannis)
pizza = Category.objects.create(name="Pizza", restaurant=giovannis)
dolci = Category.objects.create(name="Dolci", restaurant=giovannis)
vino = Category.objects.create(name="Vino", restaurant=giovannis)

MenuItem.objects.create(
    name="Garlic Bread",
    description="Toasted bread with cheese, garlic, and basil",
    price=1200,
    category=starter,
    is_available=True
)

MenuItem.objects.create(
    name="Antipasto Italiano",
    description="Cheese, salami, parma ham, pepperoni, blue cheese, black olives, and bread.",
    price=1200,
    category=starter,
    is_available=True
)

MenuItem.objects.create(
    name="Coteletto Di Pollo",
    description="Chicken crumbed with cheese and rucola.",
    price=1200,
    category=starter,
    is_available=True
)
MenuItem.objects.create(
    name="Carbonara",
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
    address="25 Kensington Garden, Colombo 00400",
    phone="+94 76 456 7890",
    email="reservations@culturecolombo.lk",
    website="https://culturecolombo.lk",
    cuisine=sri_lankan,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.882272694908216,
    longitude=79.86126396863745,
    image="media/restaurant_images/culture_colombo.jpg",
    user=culture_manager
)

# Culture Colombo Menu
soup = Category.objects.create(name="Soup", restaurant=culture_colombo)
dinner_menu = Category.objects.create(
    name="Dinner Menu", restaurant=culture_colombo)
seafood = Category.objects.create(
    name="Seafood Specialties", restaurant=culture_colombo)
desserts = Category.objects.create(
    name="Traditional Desserts", restaurant=culture_colombo)
beverages = Category.objects.create(
    name="Traditional Beverages", restaurant=culture_colombo)

MenuItem.objects.create(
    name="Vegetable Soup",
    description="Farm Fresh Vegetable soup with a pinch of salt for your liking.",
    price=850,
    category=soup,
    is_available=True
)
MenuItem.objects.create(
    name="Sweet Corn Chicken Soup",
    description="Sweet corn kernels in a flavourful chicken soup with egg drop.hicken crumbed with cheese and rucola.",
    price=1050,
    category=soup,
    is_available=True
)
MenuItem.objects.create(
    name="Pittu",
    description="A Local favourite & a regular. 3 pieces of Red or White Pittu served Kirihodi, Lunumiris, Coconut Milk & chefs dedicated Vegetable Dish.",
    price=650,
    category=dinner_menu,
    is_available=True
)
MenuItem.objects.create(
    name="String Hoppers",
    description="It’s an all rounder dish that a Sri Lankan would have for all 3 meals. 15 Nos Red or White String Hoppers served with the local favourite Kiri Hodi, Pol Sambol & chefs dedicated Vegetable Dish.",
    price=650,
    category=dinner_menu,
    is_available=True
)
MenuItem.objects.create(
    name="Culture Special Chicken Kottu",
    description="Kottu Rotti softend and Soaked in a thick curry, topped with 2 type of cheese sauce to bring the cheesiest kottu in town.",
    price=2750,
    category=dinner_menu,
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
    name="Hopper Mousse",
    description="3 scoops of mousse served on a delicious Pani appa",
    price=950,
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
    description="The monsoons in South East Asian countries affect the style of food cooked across the region, from the way it is sourced to how it is prepared and consumed. At Monsoon Colombo, we revel in the variety of opportunities this offers us!",
    address="50/2 Park Street, Colombo 00200",
    phone="+94 11 230 2449",
    email="reservations@monsooncolombo.com",
    website="https://www.monsooncolombo.com",
    cuisine=international,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.916694911661506,
    longitude=79.85849804410529,
    image="media/restaurant_images/monsoon.jpg",
    user=monsoon_manager
)

# Monsoon Colombo Menu
starters = Category.objects.create(name="Starters", restaurant=monsoon)
mains = Category.objects.create(name="Rice & Noodle Sets", restaurant=monsoon)
sides = Category.objects.create(name="Boa Buns", restaurant=monsoon)
desserts = Category.objects.create(name="Desserts", restaurant=monsoon)
cocktails = Category.objects.create(
    name="Signature Cocktails", restaurant=monsoon)

MenuItem.objects.create(
    name="Thai Papaya Salad",
    description="Som Tum Thai | dried shrimp . chilli . fresh lime dressing",
    price=1450,
    category=starters,
    is_available=True
)
MenuItem.objects.create(
    name="Crispy Duck & Mushroom Wonton",
    description="Shiitake mushroom . homemade sweet chilli dip",
    price=2450,
    category=starters,
    is_available=True
)
MenuItem.objects.create(
    name="Nasi Lemak",
    description="Malaysian beef rendang . crispy fried anchovies . boiled egg toasted peanut . cucumber . sambal badjak . coconut milk rice",
    price=3450,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Pad Thai",
    description="Stir-fried rice noodles with prawns and peanuts",
    price=2950,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Hainanese Chicken Rice",
    description="Fresh ginger sauce . chilli sauce . sweet soya sauce . chicken broth",
    price=2950,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Grilled Honey & Sriracha Chicken",
    description="Toasted sesame . sriracha mayo . spring onion",
    price=950,
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
    name=user1.first_name + " " + user1.last_name,
    rating=4.5,
    comment="Amazing Italian food! The pasta was perfect and the service was excellent."
)

Review.objects.create(
    restaurant=giovannis,
    user=user2,
    name=user2.first_name + " " + user2.last_name,
    rating=5.0,
    comment="Best pizza in Colombo! The atmosphere is lovely and the staff is very friendly."
)

Review.objects.create(
    restaurant=giovannis,
    user=user3,
    name=user3.first_name + " " + user3.last_name,
    rating=4.0,
    comment="Great food but a bit pricey. The wine selection is impressive."
)

# Culture Colombo Reviews
Review.objects.create(
    restaurant=culture_colombo,
    user=user4,
    name=user4.first_name + " " + user4.last_name,
    rating=5.0,
    comment="Authentic Sri Lankan cuisine at its best! The hoppers were amazing."
)

Review.objects.create(
    restaurant=culture_colombo,
    user=user5,
    name=user5.first_name + " " + user5.last_name,
    rating=4.5,
    comment="Loved the traditional rice and curry. The service was excellent."
)

Review.objects.create(
    restaurant=culture_colombo,
    user=user1,
    name=user1.first_name + " " + user1.last_name,
    rating=4.0,
    comment="Great place to experience local cuisine. The seafood dishes are outstanding."
)

# Monsoon Colombo Reviews
Review.objects.create(
    restaurant=monsoon,
    user=user2,
    name=user2.first_name + " " + user2.last_name,
    rating=4.5,
    comment="Beautiful fusion cuisine. The cocktails are creative and delicious."
)

Review.objects.create(
    restaurant=monsoon,
    user=user3,
    name=user3.first_name + " " + user3.last_name,
    rating=5.0,
    comment="One of my favorite restaurants in Colombo. The beef rendang is a must-try!"
)

Review.objects.create(
    restaurant=monsoon,
    user=user4,
    name=user4.first_name + " " + user4.last_name,
    rating=4.0,
    comment="Great atmosphere and food. The service could be a bit faster though."
)
