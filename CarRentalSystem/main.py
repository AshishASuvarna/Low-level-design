from datetime import date, timedelta

from Car import Car
from Customer import Customer
from RentalService import RentalService
from CarRentalSystem import CarRentalSystem
from Payment import CashPaymentStrategy, CardPaymentStrategy
from Search import SearchByPrice, SearchByCapacity

def main():
    # Setup
    rental_service = RentalService()
    system = CarRentalSystem.get_instance(rental_service)

    # Add customers
    customer1 = Customer("DL12345", "Ashish", "ashish@email.com")
    system.add_customer(customer1)

    # Add cars
    car1 = Car("KA01AB1234", "Honda City", 2022, "Honda", 50, 5)
    car2 = Car("KA01XY5678", "Maruti Swift", 2021, "Maruti", 40, 4)
    car3 = Car("KA02JK1111", "Toyota Fortuner", 2023, "Toyota", 100, 7)

    system.add_car(car1)
    system.add_car(car2)
    system.add_car(car3)

    # Search by price
    print("\nSearch cars with price <= 50:")
    cheap_cars = system.search(SearchByPrice(), 50)
    for car in cheap_cars:
        print(f"{car.get_model()} - ${car.get_price_per_day()} per day")

    # Rent a car
    print("\n--- Renting a car ---")
    start_date = date.today()
    end_date = start_date + timedelta(days=3)  # 4 days
    booking = system.rent(car1, customer1, start_date, end_date, CardPaymentStrategy())

    # Try to rent same car during same period (should fail)
    try:
        print("\n--- Trying to book the same car again ---")
        system.rent(car1, customer1, start_date, end_date, CashPaymentStrategy())
    except Exception as e:
        print(f"Expected error: {e}")

    # Cancel booking
    print("\n--- Cancel Booking ---")
    rental_service.cancel_booking(booking.get_booking_id())

    # Modify booking (rebook and then modify)
    print("\n--- Re-book and Modify Booking ---")
    new_booking = system.rent(car2, customer1, start_date, end_date, CashPaymentStrategy())

    # Modify booking: change car and dates
    new_start_date = start_date + timedelta(days=1)
    new_end_date = end_date + timedelta(days=1)

    rental_service.modify_booking(
        new_booking.get_booking_id(),
        new_car=car3,
        new_start_date=new_start_date,
        new_end_date=new_end_date,
        payment_strategy=CardPaymentStrategy()
    )

if __name__ == "__main__":
    main()
