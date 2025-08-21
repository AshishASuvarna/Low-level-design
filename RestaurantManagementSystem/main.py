from datetime import datetime
from RestaurantManagement import RestaurantManager
from Table import Table
from Ingredient import Ingredient
from Item import Item
from Staff import Staff
from Roles import Roles
from TableSearch import Searching,AvailableTableStrategy

# Get singleton instance
restaurant = RestaurantManager.get_instance()

# Add tables
restaurant.add_table(Table(1, 4))
restaurant.add_table(Table(2, 2))

# Add ingredients
restaurant.inventory_service.add_ingredient(Ingredient("bun", "Bun", 10))
restaurant.inventory_service.add_ingredient(Ingredient("patty", "Patty", 10))

# Add item to menu
burger = Item("burger", "Burger", 5.0, "Veg Burger", {"bun": 1, "patty": 1})
restaurant.menu.add_item_to_menu(burger)

# Add staff
waiter = Staff("w1", "Alice", Roles.WAITER)
manager = Staff("m1", "Bob", Roles.MANAGER)

restaurant.staff_services.add_staff(waiter)
restaurant.staff_services.add_staff(manager)

# Manager makes a reservation
reservation_data = {
    "reservation_id": "res001",
    "table": restaurant.get_table(1),
    "customer_name": "John",
    "date_time": datetime(2025, 8, 22, 18, 0)
}
restaurant.staff_services.handle_reservation(manager, "make", reservation_data, restaurant.get_all_tables())

# Waiter places an order
order = restaurant.staff_services.take_order(waiter, 2, {burger: 2})

# Waiter serves the order
if order:
    restaurant.staff_services.serve_food(waiter, order.order_id)

# Manager cancels the reservation
cancel_data = {"reservation_id": "res001"}
restaurant.staff_services.handle_reservation(manager, "cancel", cancel_data, restaurant.get_all_tables())

# Show available tables after cancellation
search_strategy = Searching(AvailableTableStrategy())
available_tables = restaurant.get_available_tables(search_strategy)
print("\n✅ Available Tables:")
for table in available_tables:
    print(f"Table {table.get_table_number()} — Available: {table.is_available}")
