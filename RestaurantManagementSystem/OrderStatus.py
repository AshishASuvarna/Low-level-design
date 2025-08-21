from enum import Enum

class OrderStatus(Enum):
    PLACED = "PLACED"
    PREPARING = "PREPARING"
    SERVED = "SERVED"
    CANCELLED = "CANCELLED"