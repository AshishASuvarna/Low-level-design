class Ingredient:
    def __init__(self,ingredient_id,name,quantity):
        self.ingredient_id=ingredient_id
        self.name=name
        self.quantity=quantity


    def refill(self, amount):
        self.quantity += amount

    def get_quantity(self):
        return self.quantity