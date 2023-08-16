class Order:
    all=[]
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price (self, new_price):
        if isinstance(new_price, int):
          self._price = new_price

from classes.customer import Customer
from classes.coffee import Coffee