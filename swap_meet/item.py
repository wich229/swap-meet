import uuid

class Item:
    # composite class to component vendor
    # attr: id = UUID_int, item
    # methods: get_by_id, get_category(from vendor)

    def __init__(self, id = 0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    

    def get_category(self):
        return str(self.__class__.__name__)



