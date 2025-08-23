from Search import SearchContext

class CarRentalSystem:
    _instance=None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.initialized=False
        return cls._instance

    @classmethod
    def get_instance(cls,rental_service):
        return cls(rental_service)

    def __init__(self,rental_service):
        if not self.initialized:
            self.cars={}
            self.customers={}
            self.rental_service=rental_service
            self.initialized=True


    def add_customer(self,customer):
        self.customers[customer.get_dl_number()]=customer

    def remove_customer(self,customer):
        self.customers.pop(customer.get_dl_number())

    def add_car(self,car):
        self.cars[car.get_license_plate()]=car

    def remove_car(self,car):
        self.cars.pop(car.get_license_plate())

    def rent(self,car,user,start_date,end_date,strategy):
        return self.rental_service.rent_a_car(car,user,start_date,end_date,strategy)

    def search(self,strategy,criteria):
        searching=SearchContext(strategy)
        return searching.search(self.cars,criteria)

    def get_available_cars(self,start_date,end_date):
        res=[]
        for car in self.cars:
            if car.is_car_available(start_date,end_date):
                res.append(car)

        if not res:
            raise Exception("No available cars at the moment")

        return res


