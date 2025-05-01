class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        self.items[product] = self.items.get(product, 0) + quantity

    def update_item(self, product, new_quantity):
        if product in self.items:
            self.items[product] = new_quantity

    def remove_item(self, product):
        self.items.pop(product, None)

    def get_quantity(self, product):
        return self.items.get(product, 0)

    def contains_product(self, product):
        return product in self.items

    def get_all_items(self):
        return self.items
