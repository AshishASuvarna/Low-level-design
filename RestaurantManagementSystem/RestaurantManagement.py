from Menu import Menu
from StaffServices import StaffServices
from ReservationServices import ReservationServices
from OrderService import OrderService
from InventoryService import InventoryService
from TableSearch import Searching

class RestaurantManager:
    _instance=None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.initialized=False

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def __init__(self):
        if not self.initialized:
            self.tables={}
            self.menu=Menu()
            self.inventory_service=InventoryService()
            self.order_service=OrderService(self.menu,self.inventory_service)

            self.reservation_services=ReservationServices()
            self.staff_services=StaffServices(self.order_service,self.reservation_services)
            self.initialized=True

    def add_table(self,table):
        self.tables[table.get_table_number()]=table

    def get_staff_service(self):
        return self.staff_services

    def get_table(self, table_number):
        return self.tables.get(table_number)

    def get_available_tables(self,strategy):
        return strategy.search(self.tables.values())

    def get_all_tables(self):
        return list(self.tables.values())