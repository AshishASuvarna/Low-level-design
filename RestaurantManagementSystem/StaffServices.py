from Roles import Roles
from OrderStatus import OrderStatus


class StaffServices:
    def __init__(self,order_service,reservation_service):
        self.order_service=order_service
        self.reservation_service=reservation_service
        self.staffs={}

    def add_staff(self, staff):
        self.staffs[staff.get_staff_id()] = staff

    def remove_staff(self, staff_id):
        if staff_id in self.staffs:
            del self.staffs[staff_id]

    def get_staff_by_role(self, role):
        return [s for s in self.staffs.values() if s.get_role() == role]

    def take_order(self,staff,table_number, ordered_items):
        #only waiter can do it
        if staff.get_role() != Roles.WAITER:
            raise PermissionError(f"{staff.get_name()} is not allowed to take orders.")
        print(f"{staff.get_name()} is taking an order.")
        return self.order_service.create_order(table_number, ordered_items)

    def serve_food(self,staff,order_id):
        #only waiter can do this
        if staff.get_role() != Roles.WAITER:
            raise PermissionError(f"{staff.get_name()} is not allowed to serve food.")

        if order_id not in self.order_service.orders:
            raise Exception("Invalid order ID")

        order=self.order_service.orders[order_id]

        if order.status != OrderStatus.PLACED:
            raise Exception(f"Order {order_id} is not ready to be served.")

        order.update_status(OrderStatus.SERVED)
        print(f"{staff.get_name()} served Order {order_id}")


    def handle_reservation(self, staff, action,reservation_data,tables):
        if staff.get_role() != Roles.MANAGER:
            raise PermissionError(f"{staff.get_name()} is not allowed to handle reservations.")
        if staff.get_role() != Roles.MANAGER:
            raise PermissionError(f"{staff.get_name()} is not allowed to handle reservations.")

        if action == "make":
            reservation_id = reservation_data["reservation_id"]
            table = reservation_data["table"]
            customer_name = reservation_data["customer_name"]
            date_time = reservation_data["date_time"]
            return self.reservation_service.reserve_a_table(reservation_id, table, customer_name, date_time)


        elif action == "cancel":
            reservation_id = reservation_data["reservation_id"]
            return self.reservation_service.cancel_a_reservation(reservation_id, tables)


        elif action == "update":
            reservation_id = reservation_data["reservation_id"]
            new_date_time = reservation_data["date_time"]
            return self.reservation_service.update_reservation(reservation_id, new_date_time)

        else:
            raise Exception("Unknown action")
