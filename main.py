import csv
class Item:
    pay_rate = 0.8 # class attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0 ):
        # Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        # better to use self.pay_rate so that we may over write the value on a different instance
        # instead of using Item.pay_rate

    # decorator
    @classmethod
    def instantiate_from_csv(cls):
        # the class itself is passed in as the first argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) # read our content as a list of dictonaries
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price, "price discounted")

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price, "price discounted")

# item2.hasNumPad = False non manditory assignments

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 10)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7.5))
x = 1