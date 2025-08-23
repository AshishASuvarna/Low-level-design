from enum import Enum

class BookingStatus(Enum):
    CANCELLED = "CANCELLED"
    BOOKED = "BOOKED"
    HOLD = "HOLD"