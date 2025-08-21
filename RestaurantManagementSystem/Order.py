import uuid
from Menu import Menu

from OrderStatus import OrderStatus

class Order:
    def __init__(self,table_number):
        self.order_id=str(uuid.uuid4())
        self.table_number=table_number
        self.ordered_items={}
        self.amount=0
        self.status = OrderStatus.PLACED

    def add_items(self,item,quantity=0):
        item_id=item.get_item_id()
        if item_id not in self.ordered_items:
            self.ordered_items[item_id]=0
        self.ordered_items[item_id]+=quantity

    def remove_items(self,item,quantity=0):
        item_id=item.get_item_id()
        if quantity==0:
            self.ordered_items.pop(item_id)
        else:
            self.ordered_items[item_id]-=quantity

    def calculate_amount(self,menu):
        total=0
        for item_id,quantity in self.ordered_items.items():
            item=menu.menu[item_id]
            price=item.get_price()
            total+=(price*quantity)
        self.amount=total
        return self.amount

    def update_status(self, new_status):
        self.status = new_status
