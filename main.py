import json

class Dish:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} x{self.quantity}'

    def __dict__(self):
        return {'name': self.name, 'quantity': self.quantity}

class Order:
    order_id = 0
    def __init__(self, table, dishes, status='pending', order_number=None):
        if order_number is None:
            Order.order_id += 1
            self.order_number = Order.order_id
        else:
            self.order_number = order_number
            self.order_id = max(self.order_id, order_number)

        self.table = table
        self.dishes = dishes
        self.status = status

    def __str__(self):
        return f'{self.table}: {", ".join([str(dish) for dish in self.dishes])}'

    def prepare(self):
        self.status = 'prepared'

    def __dict__(self):
        return {'order_number': self.order_number, 'table': self.table, 'dishes': [dish.__dict__() for dish in self.dishes], 'status': self.status}


class DishController:

    __file_path = 'orders.json'

    def __init__(self):
        self.orders = []

    def save(self):
        with open(self.__file_path, 'w') as file:
            print([order.__dict__() for order in self.orders])
            json.dump([order.__dict__() for order in self.orders], file)

    def load(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.orders = [Order(
                   table= order['table'],
                   dishes= [Dish(dish['name'], dish['quantity']) for dish in order['dishes']],
                   status= order['status']
                ) for order in data]
        except FileNotFoundError:
            print('File not found')


    def get_order_by_number(self, number):

        idx = -1
        for i in range(len(self.orders)):
            if self.orders[i].order_number == number:
                idx = i
                break

        return idx

    def add(self, order):
        self.orders.append(order)
        self.save()

    def get(self, number):
        idx = self.get_order_by_number(number)
        if idx == -1:
            return None

        return self.orders[idx]

    def remove(self, number):
        idx = self.get_order_by_number(number)
        if idx == -1:
            return False

        self.orders.pop(idx)
        self.save()
        return True

    def prepare(self, number):
        idx = self.get_order_by_number(number)
        if idx == -1:
            return False

        self.orders[idx].prepare()
        self.save()
        return True

class OrderView:
    def __init__(self, controller):
        self.controller = controller

    def add_order(self, table, dishes):
        order = Order(table, dishes)
        self.controller.add(order)

    def remove_order(self, number):
        return self.controller.remove(number)

    def prepare_order(self, number):
        return self.controller.prepare(number)


    def get_order(self, number):
        return self.controller.get(number)

    def show_all_orders(self):
        for order in self.controller.orders:
            print(order)

    def show_order(self, number):
        order = self.controller.get(number)
        if order:
            print(order)
        else:
            print('Order not found')

    def show_orders_info(self):
        pending = 0
        prepared = 0
        for order in self.controller.orders:
            if order.status == 'pending':
                pending += 1
            else:
                prepared += 1
        print(f'Pending orders: {pending}')
        print(f'Prepared orders: {prepared}')


    def run(self):

        self.controller.load()

        while True:
            print('1. Add order')
            print('2. Remove order')
            print('3. Prepare order')
            print('4. Show all orders')
            print('5. Show order')
            print('6. Show orders info')
            print('0. Exit')
            choice = input('Enter choice: ')
            if choice == '1':
                table = input('Enter table: ')
                dishes = []
                while True:
                    name = input('Enter dish name: ')
                    quantity = int(input('Enter quantity: '))
                    dishes.append(Dish(name, quantity))
                    if input('Add another dish? (y/n) ') == 'n':
                        break
                self.add_order(table, dishes)
            elif choice == '2':
                number = int(input('Enter order number: '))
                if self.remove_order(number):
                    print('Order removed')
                else:
                    print('Order not found')
            elif choice == '3':
                number = int(input('Enter order number: '))
                if self.prepare_order(number):
                    print('Order prepared')
                else:
                    print('Order not found')
            elif choice == '4':
                self.show_all_orders()
            elif choice == '5':
                number = int(input('Enter order number: '))
                self.show_order(number)
            elif choice == '6':
                self.show_orders_info()
            elif choice == '0':
                break
            else:
                print('Invalid choice')


controller = DishController()
view = OrderView(controller)
view.run()
