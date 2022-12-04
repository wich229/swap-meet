import uuid


class Item:

    def __init__(self, id = None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    
    def get_category(self):
        return str(self.__class__.__name__)
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"





