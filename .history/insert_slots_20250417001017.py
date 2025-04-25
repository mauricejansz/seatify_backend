from restaurants.models import Restaurant, Table, Slot
from datetime import datetime, time, timedelta
import pytz


def create_slots():
    # Get all restaurants
    restaurants = Restaurant.objects.all()

    # Define time slots (6 slots per day)
    time_slots = [
        time(11, 0),  # 11:00 AM
        time(13, 0),  # 1:00 PM
        time(15, 0),  # 3:00 PM
        time(17, 0),  # 5:00 PM
        time(19, 0),  # 7:00 PM
        time(21, 0),  # 9:00 PM
    ]

    # Define date range
    start_date = datetime(2025, 4, 17).date()
    end_date = datetime(2025, 5, 10).date()

    # Create slots for each restaurant
    for restaurant in restaurants:
        print(f"Creating slots for {restaurant.name}...")

        # Get or create tables for the restaurant
        # Create 3 tables with different capacities
        table1, _ = Table.objects.get_or_create(
            restaurant=restaurant,
            number="1",
            defaults={"capacity": 2}
        )
        table2, _ = Table.objects.get_or_create(
            restaurant=restaurant,
            number="2",
            defaults={"capacity": 4}
        )
        table3, _ = Table.objects.get_or_create(
            restaurant=restaurant,
            number="3",
            defaults={"capacity": 6}
        )

        tables = [table1, table2, table3]

        # Create slots for each day in the range
        current_date = start_date
        while current_date <= end_date:
            # Skip if it's a Monday (assuming restaurants are closed on Mondays)
            if current_date.weekday() != 0:  # 0 is Monday
                for table in tables:
                    for slot_time in time_slots:
                        # Create the slot
                        Slot.objects.get_or_create(
                            table=table,
                            date=current_date,
                            time=slot_time,
                            defaults={
                                "status": "available",
                                "customer_name": None
                            }
                        )

            current_date += timedelta(days=1)

        print(f"Created slots for {restaurant.name}")


if __name__ == "__main__":
    create_slots()
    print("Finished creating slots for all restaurants")
