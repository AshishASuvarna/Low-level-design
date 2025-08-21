class Table:
    def __init__(self,number,capacity):
        self.number=number
        self.capacity=capacity
        self.is_available=True


    def get_table_number(self):
        return self.number

    def get_capacity(self):
        return self.capacity

    def check_availability(self):
        return self.is_available

