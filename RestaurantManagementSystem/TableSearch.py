from abc import ABC,abstractmethod

class TableSearchStrategy(ABC):
    @abstractmethod
    def search(self,tables,**kwargs):
        pass

class AvailableTableStrategy(TableSearchStrategy):
    def search(self, tables, **kwargs):
        return [table for table in tables if table.check_availability()]

class Searching:
    def __init__(self,strategy):
        self.strategy=strategy

    def set_strategy(self,strategy):
        self.strategy=strategy

    def search(self,tables,**kwargs):
        return self.strategy.search(tables,**kwargs)