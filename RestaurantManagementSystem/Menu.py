class Menu:
    def __init__(self):
        self.menu={}

    def add_item_to_menu(self,item):
        self.menu[item.get_item_id()]=item

    def remove_item_from_menu(self,item):
        self.menu.pop(item.get_item_id())

