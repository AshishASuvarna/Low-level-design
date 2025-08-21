
# Restaurant Management System (Low-Level Design)

This project implements a backend system for managing a restaurant's operations using object-oriented design and common design patterns.

---

## 💼 Functional Requirements

- Customers can view the menu and reserve a table
- Staff (waiters) can place and serve orders
- The system should:
  - Manage reservations and table availability
  - Track inventory (ingredients) and deduct on order placement
  - Handle payments via different methods
  - Support multiple staff roles with permission controls
  - Allow searching available tables
  - Be extensible and follow solid LLD principles

---

## 🧱 Class Breakdown

### 🪑 `Table`
- Fields: `number`, `capacity`, `is_available`
- Methods: `get_table_number()`, `get_capacity()`, `check_availability()`

### 📅 `Reservation`
- Fields: `reservation_id`, `table_number`, `customer_name`, `date_time`
- Methods: Getters for each field

### 🧂 `Ingredient`
- Fields: `ingredient_id`, `name`, `quantity`
- Methods: `refill(amount)`, `get_quantity()`

### 🍽️ `Item`
- Fields: `item_id`, `name`, `price`, `description`, `recipe`
- Methods: `get_item_id()`, `get_price()`, `update_price(price)`

### 📋 `Menu`
- Methods: `add_item_to_menu(item)`, `remove_item_from_menu(item)`

### 🛒 `Order`
- Fields: `order_id`, `table_number`, `ordered_items`, `amount`, `status`
- Methods: `add_items(item, quantity)`, `remove_items(item, quantity)`, `calculate_amount(menu)`, `update_status(status)`

### 🧾 `OrderService`
- Methods: `create_order(table_number, ordered_items)`, `cancel_order(order_id)`

### 📦 `InventoryService`
- Methods: `add_ingredient(ingredient)`, `refill_ingredient(id, amount)`, `can_ful_fill(requirements)`, `deduct(requirements)`, `restock(requirements)`

### 💳 `Payment` (Strategy Pattern)
- Classes: `CashPaymentStrategy`, `CardPaymentStrategy`
- Methods: `make_payment(amount)`, `set_strategy(strategy)`

### 🧑‍🍳 `Staff`
- Fields: `staff_id`, `name`, `role` (Enum: `WAITER`, `MANAGER`)
- Methods: Getters

### 👨‍✈️ `StaffServices`
- Role-based methods: `take_order()`, `serve_food()`, `handle_reservation()`

### 🧭 `TableSearchStrategy` (Strategy Pattern)
- Strategies: `AvailableTableStrategy`
- Wrapper: `Searching`

### 🧠 `RestaurantManager` (Singleton)
- Manages: `Menu`, `InventoryService`, `OrderService`, `ReservationServices`, `StaffServices`, tables
- Methods: `add_table()`, `get_table()`, `get_all_tables()`, `get_available_tables(strategy)`

---

## 🧰 Design Patterns Used

- **Singleton** — `RestaurantManager`
- **Strategy** — `PaymentStrategy`, `TableSearchStrategy`
- **Enum** — Roles (`WAITER`, `MANAGER`) and order status (`PLACED`, `SERVED`, etc.)
- **Separation of Concerns** — Service classes for reservations, orders, inventory, staff

---

## 🚀 Getting Started

1. **Clone the repo**:
```bash
git clone https://github.com/AshishASuvarna/Low-level-design.git
cd Low-level-design/restaurantmanagementsystem
```

2. **Run the main file**:
```bash
python main.py
```

---

## 🧪 Sample Usage Flow (from `main.py`)

```python
# Manager makes a reservation
staff_service.handle_reservation(manager, "make", {
    "reservation_id": "res001",
    "table": rm.get_table(1),
    "customer_name": "John",
    "date_time": datetime(2025, 8, 22, 18, 0)
}, rm.get_all_tables())

# Waiter places and serves an order
order = staff_service.take_order(waiter, 2, {burger: 2})
if order:
    staff_service.serve_food(waiter, order.order_id)
```

---

## 📌 Future Enhancements

- Table state machine (State pattern)
- Role factory for staff creation
- Observer for kitchen notifications
- Reporting module
- CLI interface or web API

---

## 👨‍💻 Author

Ashish A. Suvarna  
Part of `Low-level-design` system design practice.
