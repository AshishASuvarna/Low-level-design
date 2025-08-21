from Order import Order
from OrderStatus import OrderStatus


class OrderService:
    def __init__(self,menu,inventory_service):
        self.menu=menu
        self.inventory_service=inventory_service

        self.orders={}

    def create_order(self,table_number,ordered_items):
        order=Order(table_number)

        for item,quantity in ordered_items.items():
            order.add_items(item,quantity)

        ingredient_requirements={}
        for item,quantity in ordered_items.items():
            if not hasattr(item, 'recipe'):
                continue
            for ing,amount in item.recipe.items():
                if ing not in ingredient_requirements:
                    ingredient_requirements[ing] = 0
                ingredient_requirements[ing]+=quantity*amount

        if not self.inventory_service.can_ful_fill(ingredient_requirements):
            print("❌ Cannot fulfill the order due to insufficient ingredients.")
            return None

        self.inventory_service.deduct(ingredient_requirements)
        order.calculate_amount(self.menu)

        order.update_status(OrderStatus.PLACED)

        self.orders[order.order_id]=order


        print(f"✅ Order {order.order_id} created for Table {table_number}")
        return order

    def cancel_order(self,order_id):
        if order_id not in self.orders:
            raise Exception("No Order")

        order = self.orders[order_id]
        ingredient_requirements={}

        for item_id,quantity in order.ordered_items.items():
            item=self.menu.menu[item_id]

            for ing_id,amount in item.recipe.items():
                if ing_id not in ingredient_requirements:
                    ingredient_requirements[ing_id] = 0
                ingredient_requirements[ing_id] += amount * quantity

        self.inventory_service.restock(ingredient_requirements)
        self.orders.pop(order_id)

        print(f"🔁 Order {order_id} cancelled and ingredients restocked.")