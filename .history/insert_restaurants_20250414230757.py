from restaurants.models import Cuisine, Restaurant, Category, MenuItem

# Create Cuisines
italian = Cuisine.objects.create(
    name="Italian", image="cuisine_images/italian.jpg", keyword="pizza, pasta, Italian, Colombo")

sri_lankan = Cuisine.objects.create(
    name="Sri Lankan", image="cuisine_images/srilankan.jpg", keyword="Sri Lankan, rice and curry, local food")

international = Cuisine.objects.create(
    name="International", image="cuisine_images/international.jpg",
    keyword="buffet, international, fusion, cuban, latin, cocktails, beach, thai, vietnamese, asian fusion")

grill_seafood = Cuisine.objects.create(
    name="Grill & Seafood", image="cuisine_images/grillseafood.jpg",
    keyword="grill, barbecue, beach restaurant, seafood, buffet, luxury dining")

fine_dining = Cuisine.objects.create(
    name="Fine Dining", image="cuisine_images/finedining.jpg",
    keyword="fine dining, rooftop, luxury")

buffet = Cuisine.objects.create(
    name="Buffet", image="cuisine_images/buffet.jpg",
    keyword="international buffet, graze, hilton")

german = Cuisine.objects.create(
    name="German", image="cuisine_images/german.jpg",
    keyword="german, beer, sausages, pork knuckle")

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
    image="media/restaurant_images/Giovannis.jpg"
)

# Giovannis Menu
antipasti = Category.objects.create(name="Antipasti", restaurant=giovannis)
pasta = Category.objects.create(name="Pasta", restaurant=giovannis)
pizza = Category.objects.create(name="Pizza", restaurant=giovannis)
dolci = Category.objects.create(name="Dolci", restaurant=giovannis)

MenuItem.objects.create(
    name="Bruschetta al Pomodoro",
    description="Toasted bread with fresh tomatoes, garlic, and basil",
    price=1200,
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
    name="Margherita Pizza",
    description="Classic pizza with tomato sauce, mozzarella, and basil",
    price=2000,
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
    image="media/restaurant_images/CultureColombo.jpg"
)

# Culture Colombo Menu
rice = Category.objects.create(name="Rice & Curry", restaurant=culture_colombo)
hoppers = Category.objects.create(
    name="Hoppers & String Hoppers", restaurant=culture_colombo)
seafood = Category.objects.create(
    name="Seafood Specialties", restaurant=culture_colombo)
desserts = Category.objects.create(
    name="Traditional Desserts", restaurant=culture_colombo)

MenuItem.objects.create(
    name="Traditional Rice & Curry",
    description="White rice with 5 curries and sambol",
    price=1500,
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
    name="Devilled Prawns",
    description="Spicy stir-fried prawns with onions and peppers",
    price=2800,
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

# 3. King of the Mambo (International)
king_mambo = Restaurant.objects.create(
    name="King of the Mambo",
    description="Latin-inspired cuisine with a modern twist",
    address="Galle Face Hotel, Colombo 03, Sri Lanka",
    phone="+94 77 222 7389",
    email="king@mambo.lk",
    website="https://kingofthemambo.lk",
    cuisine=international,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9271,
    longitude=79.8465,
    image="media/restaurant_images/KingMambo.jpg"
)

# King of the Mambo Menu
starters = Category.objects.create(name="Tapas", restaurant=king_mambo)
mains = Category.objects.create(name="Main Courses", restaurant=king_mambo)
sides = Category.objects.create(name="Sides", restaurant=king_mambo)
desserts = Category.objects.create(name="Desserts", restaurant=king_mambo)

MenuItem.objects.create(
    name="Cuban Sliders",
    description="Mini pulled pork sandwiches with mojo sauce",
    price=1800,
    category=starters,
    is_available=True
)
MenuItem.objects.create(
    name="Ropa Vieja",
    description="Traditional Cuban shredded beef with rice and beans",
    price=2800,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Plantain Chips",
    description="Crispy fried plantains with garlic aioli",
    price=900,
    category=sides,
    is_available=True
)
MenuItem.objects.create(
    name="Tres Leches Cake",
    description="Traditional Latin American sponge cake",
    price=1200,
    category=desserts,
    is_available=True
)

# 4. Harbor Court (Grill & Seafood)
harbor_court = Restaurant.objects.create(
    name="Harbor Court",
    description="Premium seafood and grill restaurant at Hilton Colombo",
    address="Hilton Colombo, Colombo 01, Sri Lanka",
    phone="+94 11 249 2492",
    email="info@harborcourt.lk",
    website="https://hiltoncolombo1.hilton.com",
    cuisine=grill_seafood,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9391,
    longitude=79.8462,
    image="media/restaurant_images/HarborCourt.jpg"
)

# Harbor Court Menu
seafood = Category.objects.create(
    name="Fresh Seafood", restaurant=harbor_court)
grill = Category.objects.create(name="From the Grill", restaurant=harbor_court)
sides = Category.objects.create(name="Sides", restaurant=harbor_court)
desserts = Category.objects.create(name="Desserts", restaurant=harbor_court)

MenuItem.objects.create(
    name="Grilled Lobster",
    description="Whole lobster with garlic butter",
    price=4500,
    category=seafood,
    is_available=True
)
MenuItem.objects.create(
    name="Ribeye Steak",
    description="300g ribeye with peppercorn sauce",
    price=3800,
    category=grill,
    is_available=True
)
MenuItem.objects.create(
    name="Grilled Vegetables",
    description="Seasonal vegetables with olive oil",
    price=1200,
    category=sides,
    is_available=True
)
MenuItem.objects.create(
    name="Key Lime Pie",
    description="Classic key lime pie with whipped cream",
    price=1300,
    category=desserts,
    is_available=True
)

# 5. Vertical By Jetwing (Fine Dining)
vertical = Restaurant.objects.create(
    name="Vertical By Jetwing",
    description="Contemporary fine dining with panoramic city views",
    address="Jetwing Colombo Seven, Colombo 07, Sri Lanka",
    phone="+94 11 255 0200",
    email="dine@vertical.lk",
    website="https://jetwinghotels.com/colomboseven",
    cuisine=fine_dining,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9152,
    longitude=79.8534,
    image="media/restaurant_images/VerticalJetwing.jpg"
)

# Vertical Menu
appetizers = Category.objects.create(name="Appetizers", restaurant=vertical)
entrees = Category.objects.create(name="Entrées", restaurant=vertical)
desserts = Category.objects.create(name="Desserts", restaurant=vertical)
wine = Category.objects.create(name="Wine Selection", restaurant=vertical)

MenuItem.objects.create(
    name="Foie Gras Terrine",
    description="Duck liver terrine with brioche and fig jam",
    price=2800,
    category=appetizers,
    is_available=True
)
MenuItem.objects.create(
    name="Wagyu Beef",
    description="A5 Japanese wagyu with truffle sauce",
    price=6500,
    category=entrees,
    is_available=True
)
MenuItem.objects.create(
    name="Soufflé",
    description="Grand Marnier soufflé with vanilla ice cream",
    price=1800,
    category=desserts,
    is_available=True
)
MenuItem.objects.create(
    name="Château Margaux",
    description="2015 Bordeaux, France",
    price=12000,
    category=wine,
    is_available=True
)

# 6. The Bavarian (German)
bavarian = Restaurant.objects.create(
    name="The Bavarian",
    description="Authentic German cuisine and beer garden",
    address="Galle Road, Colombo 03, Sri Lanka",
    phone="+94 11 243 3523",
    email="info@bavarian.lk",
    website="https://bavarian.lk",
    cuisine=german,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9248,
    longitude=79.8630,
    image="media/restaurant_images/Bavarian.jpg"
)

# Bavarian Menu
starters = Category.objects.create(name="Starters", restaurant=bavarian)
mains = Category.objects.create(name="Main Courses", restaurant=bavarian)
beer = Category.objects.create(name="Beer Selection", restaurant=bavarian)
desserts = Category.objects.create(name="Desserts", restaurant=bavarian)

MenuItem.objects.create(
    name="Bavarian Pretzel",
    description="Traditional German pretzel with mustard",
    price=800,
    category=starters,
    is_available=True
)
MenuItem.objects.create(
    name="Pork Knuckle",
    description="Crispy pork knuckle with sauerkraut and potatoes",
    price=2800,
    category=mains,
    is_available=True
)
MenuItem.objects.create(
    name="Weissbier",
    description="Traditional German wheat beer",
    price=1200,
    category=beer,
    is_available=True
)
MenuItem.objects.create(
    name="Apple Strudel",
    description="Traditional German apple strudel with vanilla sauce",
    price=1100,
    category=desserts,
    is_available=True
)
