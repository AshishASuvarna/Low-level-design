from threading import Lock

from Booking import Booking
from Payment import Payment
from BookingStatus import BookingStatus

class RentalService:
    def __init__(self):
        self.rent_bookings={}
        self.lock=Lock()

    def rent_a_car(self,car,customer,start_date,end_date,payment_strategy):
        with self.lock:
            if not car.is_car_available(start_date,end_date):
                raise Exception("Car not available")

            price=car.get_price_per_day()
            days=(end_date-start_date).days+1
            amount=price*days
            booking=Booking(car,customer,start_date,end_date,amount)

            payment=Payment(payment_strategy)
            payment.make_payment(amount)

            booking.confirm_booking()

            booking_id=booking.get_booking_id()
            self.rent_bookings[booking_id]=booking
            car.bookings[booking_id]=booking

            print(f"{car.get_model()}-{car.get_license_plate()} has been booked by {customer.get_name()}")

            return booking

    def cancel_booking(self,booking_id):
        with self.lock:
            booking=self.rent_bookings.get(booking_id)

            if not booking:
                raise Exception("Booking not found")

            car=booking.get_car()

            booking.status=BookingStatus.CANCELLED

        #this we need when want to remove the history of bookings but if we set status as cancelled it is ignored!
        # car.bookings.pop(booking_id)
        # self.rent_bookings.pop(booking_id)

        print(f"{booking_id} has been Cancelled. Car: {car.get_model()}-{car.get_license_plate()} is available.")


    def modify_booking(self,booking_id,new_car=None,new_start_date=None,new_end_date=None,payment_strategy=None):
        with self.lock:
            booking = self.rent_bookings.get(booking_id)
            if not booking:
                raise Exception("Booking not found")

            old_car = booking.get_car()
            start_date = new_start_date or booking.get_start_date()
            end_date = new_end_date or booking.get_end_date()
            car = new_car or old_car

            # Check availability of the new car (exclude this booking's own range)
            for other_booking in car.get_bookings().values():
                if other_booking.get_booking_id() == booking_id or other_booking.status != BookingStatus.BOOKED:
                    continue
                if not (end_date <= other_booking.get_start_date() or start_date >= other_booking.get_end_date()):
                    raise Exception("Selected car is not available in the new date range")

            # Update car if changed
            if new_car and new_car != old_car:
                # Remove from old car
                old_car.get_bookings().pop(booking_id, None)
                # Add to new car
                new_car.add_bookings(booking)
                booking.car = new_car

            # Update dates and recalculate amount
            # Recalculate amount
            new_days = (end_date - start_date).days + 1
            new_amount = car.get_price_per_day() * new_days

            old_amount = booking.amount
            booking.start_date = start_date
            booking.end_date = end_date
            booking.amount = new_amount

            # Handle payment difference
            if new_amount > old_amount:
                difference = new_amount - old_amount
                print(f"Additional payment of ${difference} required.")
                if payment_strategy:
                    payment = Payment(payment_strategy)
                    payment.make_payment(difference)
                else:
                    print("No payment strategy provided. Please pay manually.")
            elif new_amount < old_amount:
                print(f"Booking amount decreased by ${old_amount - new_amount}. (Refund logic not implemented)")

            print(f"Booking {booking_id} has been modified successfully.")


