
class Vendor:
    # composite class to component item
    # constructors: name, inventory, item
    # methods : add, remove, get_by_id

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []


    def add(self, item):
        if item is not None:
            self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        if item is not None:
            self.inventory.remove(item)
            return item

    def get_by_id(self, id):
        if not self.inventory:
            return None

        for item in self.inventory:
            if id == item.id:
                return item