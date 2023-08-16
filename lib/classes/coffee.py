class Coffee:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2< len(new_name) and not hasattr(self, "name"):
          self._name = new_name

    def orders(self):
        new_list=[]
        for obj in Order.all:
            if obj.coffee == self:
                new_list.append(obj)
        return new_list
    
    def customers(self):
        new_list=[]
        for obj in Order.all:
            if obj.coffee == self:
                new_list.append(obj.customer)
        return list(set(new_list))
    
    def num_orders(self):
        new_list=[]
        for obj in Order.all:
            if obj.coffee == self:
                new_list.append(obj)
        return len(new_list)
    
    def average_price(self):
        total=0
        count=0
        for obj in Order.all:
            if obj.coffee == self:
                total += obj.price
                count += 1
        return total/count

from classes.order import Order