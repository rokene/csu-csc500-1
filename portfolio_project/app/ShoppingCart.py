class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020", force_confirmation=False):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        self.force_confirmation = force_confirmation

    def addItem(self, item):
        self.cart_items.append(item)

    def removeItem(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modifyItem(self, item_name, item_qty):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = item_qty
                return
        print("Item not found in cart. Nothing modified.")

    def getNumItemsInCart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def getCostOfCart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def printTotal(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.getNumItemsInCart()}")
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}")
        print(f"Total: ${self.getCostOfCart()}")

    def printDescriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
