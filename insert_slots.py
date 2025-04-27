from restaurants.models import Restaurant, Table, Slot
from datetime import datetime, time, timedelta

print("Starting slot creation script...")


def create_slots():
    # Get all restaurants
    restaurants = Restaurant.objects.all()
    print(f"Found {restaurants.count()} restaurants")

    # Define time slots (6 slots per day)
    time_slots = [
        time(20, 0),  # 5:00 PM
        time(19, 0),  # 7:00 PM
        time(21, 0),  # 9:00 PM
    ]

    # Define date range
    start_date = datetime(2025, 4, 27).date()
    end_date = datetime(2025, 5, 10).date()
    print(f"Creating slots from {start_date} to {end_date}")

    # Create slots for each restaurant
    for restaurant in restaurants:
        print(f"\nCreating slots for {restaurant.name}...")

        # Get or create tables for the restaurant
        # Create 3 tables with different capacities
        table1, created = Table.objects.get_or_create(
            restaurant=restaurant,
            number="1",
            defaults={"capacity": 2}
        )
        print(f"Table 1 {'created' if created else 'already exists'}")

        table2, created = Table.objects.get_or_create(
            restaurant=restaurant,
            number="2",
            defaults={"capacity": 4}
        )
        print(f"Table 2 {'created' if created else 'already exists'}")

        table3, created = Table.objects.get_or_create(
            restaurant=restaurant,
            number="3",
            defaults={"capacity": 6}
        )
        print(f"Table 3 {'created' if created else 'already exists'}")

        tables = [table1, table2, table3]

        # Create slots for each day in the range
        current_date = start_date
        slots_created = 0
        while current_date <= end_date:
            # Skip if it's a Monday (assuming restaurants are closed on Mondays)
            if current_date.weekday() != 0:  # 0 is Monday
                for table in tables:
                    for slot_time in time_slots:
                        # Create the slot
                        slot, created = Slot.objects.get_or_create(
                            table=table,
                            date=current_date,
                            time=slot_time,
                            defaults={
                                "status": "available",
                                "customer_name": None
                            }
                        )
                        if created:
                            slots_created += 1

            current_date += timedelta(days=1)

        print(f"Created {slots_created} slots for {restaurant.name}")


print("Executing create_slots()...")
create_slots()
print("Finished creating slots for all restaurants")
