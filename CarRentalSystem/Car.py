from BookingStatus import BookingStatus
class Car:
    def __init__(self,license_plate,model,year,make,price_per_day,capacity):
        self.license_plate=license_plate
        self.model=model
        self.year=year
        self.make=make

        self.price_per_day=price_per_day
        self.capacity=capacity

        self.bookings={}

    def get_license_plate(self):
        return self.license_plate

    def get_model(self):
        return self.model

    def get_price_per_day(self):
        return self.price_per_day

    def get_year(self):
        return self.year

    def get_make(self):
        return self.make

    def get_capacity(self):
        return self.capacity



    def get_bookings(self):
        return self.bookings

    def add_bookings(self,booking):
        self.bookings[booking.booking_id]=booking

    def is_car_available(self,start_date,end_date):
        for booking in self.bookings.values():
            if booking.status in [BookingStatus.HOLD, BookingStatus.BOOKED]:
                if not (start_date>=booking.end_date or end_date<=booking.start_date):
                    return False

        return True
