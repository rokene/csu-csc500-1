class ItemToPurchase:

    def __init__(
        self,
        item_name="none",
        item_price=0.0,
        item_quantity=0,
        item_description=""):

        self.item_name = item_name
        self.item_price = round(float(item_price), 2)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}')
