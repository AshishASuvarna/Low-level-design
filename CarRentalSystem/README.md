# 🚗 Car Rental System - Low-Level Design (LLD)

This project is a Low-Level Design (LLD) implementation of a **Car Rental System** using Python. It simulates a simple rental platform where customers can search, rent, cancel, or modify car bookings.

---

## ✅ Functional Requirements

1. Customers can **browse and rent** available cars for specific dates.
2. Customers can **cancel or modify** their bookings.
3. Multiple **payment methods** (Cash, Card) are supported.
4. Customers can **search** for cars based on:
   - Price
   - Capacity
5. Each car has:
   - License plate, model, price per day, make, year, capacity.
6. The system tracks:
   - Customer details (name, email, driver's license)
   - Booking details (dates, amount, car, status)

---

## 🧱 Core Entities

| Entity    | Attributes / Methods |
|-----------|-----------------------|
| **Customer** | dl_number, name, email |
| **Car**       | license_plate, model, year, make, capacity, price_per_day, status, bookings |
| **Booking**   | booking_id, car, customer, start_date, end_date, amount, status |
| **Payment**   | Uses `PaymentStrategy` (Cash or Card) to process payments |
| **RentalService** | Handles rent, cancel, and modify operations |
| **CarRentalSystem** | System entry point; holds customers and cars |
| **Search**    | Uses strategy pattern to search by price or capacity |

---

## 🎯 Design Patterns Used

| Pattern       | Where It’s Used                        | Purpose |
|---------------|----------------------------------------|---------|
| **Singleton** | `CarRentalSystem`                     | Ensure only one instance manages system state |
| **Strategy**  | `PaymentStrategy`, `SearchStrategy`   | Easily extend search and payment logic |
| **Enum**      | `BookingStatus`                       | Manage booking lifecycle (`HOLD`, `BOOKED`, `CANCELLED`) |

---

## 🏁 Booking Flow

```text
Customer → Search → Select Car → Rent → Pay → Booking Confirmed
Bookings are rejected if car is already booked in the requested date range.

Modifications support updating car or booking dates.

If the new price is higher, user is prompted to pay the difference.

🚀 How to Run
Clone the repo:

git clone https://github.com/AshishASuvarna/Low-level-design.git
Navigate to the project:

cd Low-level-design/CarRentalSystem
Run the program:

python3 main.py
📌 Example Features Demonstrated in main.py
Adding cars and customers

Searching for cars by price

Booking and payment flow

Attempting overlapping bookings

Canceling a booking

Modifying a booking (including payment diff)

📁 Project Structure

CarRentalSystem/
├── Car.py
├── Customer.py
├── Booking.py
├── Payment.py
├── RentalService.py
├── CarRentalSystem.py
├── Search.py
├── BookingStatus.py
├── main.py
├── .gitignore
└── README.md

🙋‍♂️ Author
Ashish Suvarna
