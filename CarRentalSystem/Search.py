from abc import ABC,abstractmethod

class SearchStrategy(ABC):
    @abstractmethod
    def search(self,cars,criteria):
        pass

class SearchByPrice(SearchStrategy):
    def search(self,cars,price):
        answer=[]
        for car in cars.values():
            if car.get_price_per_day()<=price:
                answer.append(car)
        if not answer:
            raise Exception("No cars found")
        return answer

class SearchByCapacity(SearchStrategy):
    def search(self,cars,capacity):
        answer=[]
        for car in cars.values():
            if car.get_capacity()>=capacity:
                answer.append(car)
        if not answer:
            raise Exception("No cars found")
        return answer

class SearchContext:
    def __init__(self,search_strategy):
        self.strategy=search_strategy

    def set_strategy(self,strategy):
        self.strategy=strategy

    def search(self,cars,criteria):
        return self.strategy.search(cars,criteria)