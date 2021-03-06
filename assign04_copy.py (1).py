#from customer import Customer
class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        count = len(self.orders)
        return count

    def get_total(self):
        total = 0
        for o in self.orders:
            total += o.get_total()
        return total

    def add_order(self,order):
        self.orders.append(order)

    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))

    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print()

        for d in self.orders:
            d.display_receipt()
            print()
       
#from order import Order       
class Order:
    def __init__(self):
        self.id = ""
        self.products = []

    def get_subtotal(self):
        total = 0
        for p in self.products:
            total += p.get_total_price()
        return total

    def get_tax(self):
        tax = self.get_subtotal() * 0.065
        return tax

    def get_total(self):
        total = self.get_subtotal() + self.get_tax()
        return total

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print("Order:{}" .format(self.id))
        for p in self.products:
            p.display()
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))

#from product import Product
class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        total_price = self.price * self.quantity
        return total_price

    def display(self):
        self.get_total_price()
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity,self.get_total_price()))        

def main():
    print("### Testing Products ###")
    p1 = Product("1238223", "Sword", 1899.99, 10)

    print("Id: {}".format(p1.id))
    print("Name: {}".format(p1.name))
    print("Price: {}".format(p1.price))
    print("Quantity: {}".format(p1.quantity))

    p1.display()

    print()

    p2 = Product("838ab883", "Shield", 989.75, 6)
    print("Id: {}".format(p2.id))
    print("Name: {}".format(p2.name))
    print("Price: {}".format(p2.price))
    print("Quantity: {}".format(p2.quantity))

    p2.display()

    print("\n### Testing Orders ###")
    # Now test Orders
    order1 = Order()
    order1.id = "1138"
    order1.add_product(p1)
    order1.add_product(p2)

    order1.display_receipt()

    print("\n### Testing Customers ###")
    # Now test customers
    c = Customer()
    c.id = "aa32"
    c.name = "Gandalf"
    c.add_order(order1)

    c.display_summary()

    print()
    c.display_receipts()

    # Add another product and order and display again

    p3 = Product("2387127", "The Ring", 1000000, 1)
    p4 = Product("1828191", "Wizard Staff", 199.99, 3)

    order2 = Order()
    order2.id = "1277182"
    order2.add_product(p3)
    order2.add_product(p4)

    c.add_order(order2)

    print()
    c.display_summary()

    print()
    c.display_receipts()


if __name__ == "__main__":
    main()