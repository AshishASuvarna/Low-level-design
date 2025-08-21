from Reservation import Reservation

class ReservationServices:
    def __init__(self):
        self.reservations={}

    def reserve_a_table(self,reservation_id,table,customer_name,date_time):
        if not table.check_availability():
            raise Exception(f"Table {table.number} is already reserved.")

        reservation = Reservation(reservation_id, table.get_table_number(), customer_name, date_time)
        self.reservations[reservation_id] = reservation
        table.is_available = False
        print(f"✅ Reserved Table {table.number} for {customer_name} on {date_time}")
        return reservation

    def cancel_a_reservation(self,reservation_id,tables):
        if reservation_id not in self.reservations:
            raise Exception("Cannot find the reservation")

        reservation = self.reservations.pop(reservation_id)
        table_number = reservation.get_table_number()

        for table in tables:
            if table.get_table_number() == table_number:
                table.is_available = True
                break

        print(f"❌ Reservation {reservation_id} canceled and table {table_number} is now available.")

    def update_reservation(self,reservation_id,new_date_time):
        if reservation_id not in self.reservations:
            raise Exception("Cannot find the reservation")

        self.reservations[reservation_id].date_time = new_date_time
        print(f"🔁 Reservation {reservation_id} updated to {new_date_time}")
