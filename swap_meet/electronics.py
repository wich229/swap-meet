from .item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.type = type
    
    
  # for option # new solution
    def compare_attrs(self, other_item):
        return self.type == other_item.type

    def __str__(self):
        return f"{super().__str__()}. This is a {self.type} device."