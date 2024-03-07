import datetime

class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock

class SimpleProduct(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        self.total_value = self.quantity_in_stock * self.unit_price
        return self.total_value

class PerishableProduct(SimpleProduct):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, product_name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date

    def calculate_value(self):
        self.total_value = self.quantity_in_stock * self.unit_price
       
        self.total_value *= 0.5
        return self.total_value

class DigitalProduct(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        self.total_value = self.quantity_in_stock * self.price
        return self.total_value
