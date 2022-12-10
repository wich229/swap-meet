from .item import Item

class Clothing(Item):
    
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.fabric = fabric
        
    # for option # new solution
    def compare_attrs(self, other_item):
        return self.fabric == other_item.fabric
    
    def __str__(self):
        return f"{super().__str__()}. It is made from {self.fabric} fabric."
