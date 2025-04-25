from restaurants.models import Restaurant, Category, MenuItem


def create_menu_items():
    # Italian Restaurants
    italian_restaurants = Restaurant.objects.filter(cuisine__name="Italian")
    for restaurant in italian_restaurants:
        # Create categories
        antipasti = Category.objects.create(
            name="Antipasti", restaurant=restaurant)
        pasta = Category.objects.create(name="Pasta", restaurant=restaurant)
        pizza = Category.objects.create(name="Pizza", restaurant=restaurant)
        dolci = Category.objects.create(name="Dolci", restaurant=restaurant)

        # Create menu items
        MenuItem.objects.create(
            name="Bruschetta al Pomodoro",
            description="Toasted bread with fresh tomatoes, garlic, and basil",
            price=1200,
            category=antipasti,
            is_available=True
        )
        MenuItem.objects.create(
            name="Calamari Fritti",
            description="Crispy fried calamari with marinara sauce",
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

    # Sri Lankan Restaurants
    sri_lankan_restaurants = Restaurant.objects.filter(
        cuisine__name="Sri Lankan")
    for restaurant in sri_lankan_restaurants:
        # Create categories
        rice = Category.objects.create(
            name="Rice & Curry", restaurant=restaurant)
        hoppers = Category.objects.create(
            name="Hoppers & String Hoppers", restaurant=restaurant)
        seafood = Category.objects.create(
            name="Seafood Specialties", restaurant=restaurant)
        desserts = Category.objects.create(
            name="Traditional Desserts", restaurant=restaurant)

        # Create menu items
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
            name="String Hoppers with Curry",
            description="Steamed rice noodles with coconut sambol and curry",
            price=1200,
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

    # International Restaurants
    international_restaurants = Restaurant.objects.filter(
        cuisine__name="International")
    for restaurant in international_restaurants:
        # Create categories
        starters = Category.objects.create(
            name="Starters", restaurant=restaurant)
        mains = Category.objects.create(
            name="Main Courses", restaurant=restaurant)
        sides = Category.objects.create(name="Sides", restaurant=restaurant)
        desserts = Category.objects.create(
            name="Desserts", restaurant=restaurant)

        # Create menu items
        MenuItem.objects.create(
            name="Crispy Calamari",
            description="Lightly battered calamari with sweet chili sauce",
            price=1800,
            category=starters,
            is_available=True
        )
        MenuItem.objects.create(
            name="Beef Tenderloin",
            description="Grilled beef tenderloin with red wine reduction",
            price=3500,
            category=mains,
            is_available=True
        )
        MenuItem.objects.create(
            name="Grilled Salmon",
            description="Fresh salmon with lemon butter sauce",
            price=3200,
            category=mains,
            is_available=True
        )
        MenuItem.objects.create(
            name="Truffle Fries",
            description="Hand-cut fries with truffle oil and parmesan",
            price=1200,
            category=sides,
            is_available=True
        )
        MenuItem.objects.create(
            name="Chocolate Lava Cake",
            description="Warm chocolate cake with vanilla ice cream",
            price=1500,
            category=desserts,
            is_available=True
        )

    # Grill & Seafood Restaurants
    grill_restaurants = Restaurant.objects.filter(
        cuisine__name="Grill & Seafood")
    for restaurant in grill_restaurants:
        # Create categories
        seafood = Category.objects.create(
            name="Fresh Seafood", restaurant=restaurant)
        grill = Category.objects.create(
            name="From the Grill", restaurant=restaurant)
        sides = Category.objects.create(name="Sides", restaurant=restaurant)
        desserts = Category.objects.create(
            name="Desserts", restaurant=restaurant)

        # Create menu items
        MenuItem.objects.create(
            name="Grilled Lobster",
            description="Whole lobster with garlic butter",
            price=4500,
            category=seafood,
            is_available=True
        )
        MenuItem.objects.create(
            name="Grilled Prawns",
            description="Jumbo prawns with lemon garlic sauce",
            price=2800,
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

    # Fine Dining Restaurants
    fine_dining_restaurants = Restaurant.objects.filter(
        cuisine__name="Fine Dining")
    for restaurant in fine_dining_restaurants:
        # Create categories
        appetizers = Category.objects.create(
            name="Appetizers", restaurant=restaurant)
        entrees = Category.objects.create(
            name="Entrées", restaurant=restaurant)
        desserts = Category.objects.create(
            name="Desserts", restaurant=restaurant)
        wine = Category.objects.create(
            name="Wine Selection", restaurant=restaurant)

        # Create menu items
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
            name="Pan-Seared Scallops",
            description="Fresh scallops with cauliflower purée",
            price=4200,
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

    # German Restaurants
    german_restaurants = Restaurant.objects.filter(cuisine__name="German")
    for restaurant in german_restaurants:
        # Create categories
        starters = Category.objects.create(
            name="Starters", restaurant=restaurant)
        mains = Category.objects.create(
            name="Main Courses", restaurant=restaurant)
        beer = Category.objects.create(
            name="Beer Selection", restaurant=restaurant)
        desserts = Category.objects.create(
            name="Desserts", restaurant=restaurant)

        # Create menu items
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
            name="Bratwurst Platter",
            description="Assorted German sausages with mustard and sauerkraut",
            price=2200,
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


if __name__ == "__main__":
    create_menu_items()
