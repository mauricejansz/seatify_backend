
from restaurants.models import Cuisine, Restaurant

italian = Cuisine.objects.create(
    name='Italian', image='cuisine_images/italian.jpg', keyword='pizza, pasta, Italian, Colombo')

sri_lankan = Cuisine.objects.create(
    name='Sri Lankan', image='cuisine_images/srilankan.jpg', keyword='Sri Lankan, rice and curry, local food')

international = Cuisine.objects.create(name='International', image='cuisine_images/international.jpg',
                                       keyword='buffet, international, fusion, cuban, latin, cocktails, beach, thai, vietnamese, asian fusion')

grill_seafood = Cuisine.objects.create(
    name='Grill & Seafood', image='cuisine_images/grillseafood.jpg', keyword='grill, barbecue, beach restaurant, seafood, buffet, luxury dining')

fine_dining = Cuisine.objects.create(
    name='Fine Dining', image='cuisine_images/finedining.jpg', keyword='fine dining, rooftop, luxury')

buffet = Cuisine.objects.create(
    name='Buffet', image='cuisine_images/buffet.jpg', keyword='international buffet, graze, hilton')

german = Cuisine.objects.create(
    name='German', image='cuisine_images/german.jpg', keyword='german, beer, sausages, pork knuckle')

Restaurant.objects.create(
    name="Giovannis",
    description="Demo restaurant entry for Giovannis",
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

Restaurant.objects.create(
    name="Culture Colombo",
    description="Demo restaurant entry for Culture Colombo",
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

Restaurant.objects.create(
    name="King of the Mambo",
    description="Demo restaurant entry for King of the Mambo",
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

Restaurant.objects.create(
    name="Plates",
    description="Demo restaurant entry for Plates",
    address="Colombo City Centre, Colombo, Sri Lanka",
    phone="+94 77 987 6543",
    email="contact@plates.lk",
    website="https://plates.lk",
    cuisine=international,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9164,
    longitude=79.8473,
    image="media/restaurant_images/Plates.jpg"
)

Restaurant.objects.create(
    name="Harbor Court",
    description="Demo restaurant entry for Harbor Court",
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

Restaurant.objects.create(
    name="Monsoon Colombo",
    description="Demo restaurant entry for Monsoon Colombo",
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
    image="media/restaurant_images/2025-01-18.jpg"
)

Restaurant.objects.create(
    name="Firebeach",
    description="Demo restaurant entry for Firebeach",
    address="Galle Face Terrace, Colombo 03, Sri Lanka",
    phone="+94 77 456 1234",
    email="hello@firebeach.lk",
    website="https://firebeach.lk",
    cuisine=grill_seafood,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9276,
    longitude=79.8492,
    image="media/restaurant_images/Firebeach.jpg"
)

Restaurant.objects.create(
    name="Vertical By Jetwing",
    description="Demo restaurant entry for Vertical By Jetwing",
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

Restaurant.objects.create(
    name="Graze Kitchen",
    description="Demo restaurant entry for Graze Kitchen",
    address="Hilton Colombo, Colombo 02, Sri Lanka",
    phone="+94 11 249 2000",
    email="graze@hilton.lk",
    website="https://hiltoncolombo1.hilton.com/graze",
    cuisine=buffet,
    lowest_price=1000.0,
    highest_price=5000.0,
    is_published=True,
    latitude=6.9266,
    longitude=79.8503,
    image="media/restaurant_images/GrazeKitchen.jpg"
)

Restaurant.objects.create(
    name="The Bavarian",
    description="Demo restaurant entry for The Bavarian",
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

Restaurant.objects.create(
    name="Rocco's",
    description="Authentic Italian wood-fired pizzas and hearty pastas in a cozy Colombo setting.",
    address="1/1 Vajira Rd, Colombo 04, Sri Lanka",
    phone="+94 11 250 2590",
    email="info@roccos.lk",
    website="https://www.roccos.lk",
    cuisine=italian,
    lowest_price=1200.0,
    highest_price=4800.0,
    is_published=True,
    latitude=6.8886,
    longitude=79.8611,
    image="media/restaurant_images/Roccos.jpg"
)

Restaurant.objects.create(
    name="Dolce Italia",
    description="Charming family-run Italian restaurant serving traditional recipes and homemade desserts.",
    address="16A, Flower Road, Colombo 07, Sri Lanka",
    phone="+94 77 012 3456",
    email="hello@dolceitalia.lk",
    website="https://dolceitalia.lk",
    cuisine=italian,
    lowest_price=1500.0,
    highest_price=5500.0,
    is_published=True,
    latitude=6.9097,
    longitude=79.8652,
    image="media/restaurant_images/DolceItalia.jpg"
)

Restaurant.objects.create(
    name="La Trattoria",
    description="Upscale Italian dining experience offering gourmet pasta, risotto, and fine wines.",
    address="Galle Face Terrace, Colombo 03, Sri Lanka",
    phone="+94 76 765 4321",
    email="reservations@latrattoria.lk",
    website="https://latrattoria.lk",
    cuisine=italian,
    lowest_price=2000.0,
    highest_price=6000.0,
    is_published=True,
    latitude=6.9261,
    longitude=79.8499,
    image="media/restaurant_images/LaTrattoria.jpg"
)
