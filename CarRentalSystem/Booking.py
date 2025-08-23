import uuid
from BookingStatus import BookingStatus

class Booking:
    def __init__(self,car, customer,start_date,end_date,amount):
        self.booking_id=str(uuid.uuid4())
        self.car=car
        self.customer=customer
        self.start_date=start_date
        self.end_date=end_date
        self.amount=amount

        self.status=BookingStatus.HOLD

    def get_booking_id(self):
        return self.booking_id

    def confirm_booking(self):
        self.status=BookingStatus.BOOKED

    def cancel_booking(self):
        self.status=BookingStatus.CANCELLED

    def get_car(self):
        return self.car

    def get_customer(self):
        return self.customer

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

