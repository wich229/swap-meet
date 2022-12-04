
class Vendor:

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
    
    def swap_items(self, other_vendor, my_item, their_item):
        # if not self.inventory or not other_vendor.inventory:
        #     return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
        
