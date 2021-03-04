'''
Oscar Enrique Gonzalez Mosqueda
CS241
'''


class Product:
    '''
    This class allows us to view and calculate the price range
    among the quantity of the product.
    '''
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        '''returns price, multiplied by the quantity'''
        total = self.price * self.quantity
        return total

    def display(self):
        '''displays the products name, quantity, and total price'''
        my_total = self.get_total_price()
        print(f'{self.name} ({self.quantity}) - ${my_total:.2f}')


class Order:
    '''
    The order class determines the price range within the specified amount of items in the order
    it will also calculate tax.
    '''
    def __init__(self):
        self.id = id
        self.products = []

    def get_subtotal(self):
        '''sums the price of each product and returns it'''
        subtotal = 0
        for sum_prices in self.products:
            subtotal += sum_prices.get_total_price()
        return subtotal

    def get_tax(self):
        '''returns 6.5% times the subtotal'''
        subtotal = self.get_subtotal()
        return 0.065 * subtotal

    def get_total(self):
        '''Returns the subtotal plus the tax'''
        tax = self.get_tax()
        subtotal = self.get_subtotal()
        return tax + subtotal

    def add_product(self, product):
        '''Adds the provided product to the list'''
        self.products.append(product)

    def display_receipt(self):
        '''Displays a receipt in the format:'''
        print(f'Order: {self.id}')
        for product in self.products:
            product.display()
        print(f'Subtotal: ${self.get_subtotal():.2f}')
        print(f'Tax: ${self.get_tax():.2f}')
        print(f'Total: ${self.get_total():.2f}')


class Customer:
    '''
    This portion of the program allows us to view the amount of orders that
    the customer placed, as well as the total items and price range of each
    order made by the customer.
    '''
    def __init__(self):
        self.id = id
        self.name = ''
        self.orders = []

    def get_order_count(self):
         # Returns the number of orders
        num_orders = len(self.orders)
        return num_orders

    def get_total(self):
        ''' Returns the total price of all orders combined'''
        total_price = 0
        for order in self.orders:
            total_price += order.get_total()
        return total_price

    def add_order(self, order):
        '''Adds the provided order to the list of orders'''
        self.orders.append(order)

    def display_summary(self):
        '''
        Displays a summary as follows:
        '''
        print(f"Summary for customer '{self.id}'")
        print(f'Name: {self.name}')
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: {self.get_total():.2f}')

    def display_receipts(self):
        '''
        Displays a receipt in the format:
        '''
        print(f"Detailed receipts for customer '{self.id}':")
        print(f'Name: {self.name}\n')
        for order in self.orders:
            order.display_receipt()
            print()



def main():
    """ Do Not Change This Function """

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
