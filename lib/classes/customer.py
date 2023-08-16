class Customer:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1< len(new_name) <15:
          self._name= new_name

    def orders(self):
        new_list=[]
        for obj in Order.all:
            if obj.customer == self:
                new_list.append(obj)
        return new_list
    
    def coffees(self):
        new_list=[]
        for obj in Order.all:
            if obj.customer == self:
                print('worked')
                new_list.append(obj.coffee)
        return list(set(new_list))
    
    def create_order(self, coffee, price):
        new_order= Order(self, coffee, price)
        return new_order
        
        


from classes.order import Order