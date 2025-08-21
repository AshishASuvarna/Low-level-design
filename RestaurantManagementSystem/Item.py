class Item:
    def __init__(self,item_id,name,price,description,recipe=None):
        self.item_id=item_id
        self.name=name
        self.price=price
        self.description=description
        self.recipe=recipe or {} #ingredient_id->quantity

    def get_item_id(self):
        return self.item_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def update_price(self,price):
        self.price=price