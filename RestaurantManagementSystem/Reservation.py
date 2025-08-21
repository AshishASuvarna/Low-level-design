class Reservation:
    def __init__(self,reservation_id,table_number,customer_name,date_time):
        self.reservation_id=reservation_id
        self.table_number=table_number
        self.customer_name=customer_name
        self.date_time=date_time

    def get_reservation_id(self):
        return self.reservation_id

    def get_table_number(self):
        return self.table_number

    def get_customer_name(self):
        return self.customer_name

    def get_date_time(self):
        return self.date_time

