class InventoryService:
    def __init__(self):
        self.inventory={}

    def add_ingredient(self, ingredient):
        self.inventory[ingredient.ingredient_id]=ingredient


    def refill_ingredient(self, ingredient_id, amount):
        if ingredient_id in self.inventory:
            self.inventory[ingredient_id].refill(amount)

    def can_ful_fill(self,ingredient_requirements):
        for ing_id,amount in ingredient_requirements.items():
            if ing_id not in self.inventory or self.inventory[ing_id].quantity<amount:
                return False
        return True

    def deduct(self,ingredient_requirements):
        for ing_id, amount in ingredient_requirements.items():
            self.inventory[ing_id].quantity-=amount

    def restock(self, ingredient_requirements):
        for ing_id, amount in ingredient_requirements.items():
            if ing_id in self.inventory:
                self.inventory[ing_id].quantity += amount