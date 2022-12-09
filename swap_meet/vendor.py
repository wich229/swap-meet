
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
        print(f"\nid: {id}\n")
        if not self.inventory:
            return None
        else:
            for item in self.inventory:
                if item.id == id:
                    return item
    
    def swap_items(self, other_vendor, my_item, their_item):
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


    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)
        return result


    def get_best_by_category(self, category):
        same_category_list = self.get_by_category(category)

        if len(same_category_list) == 0:
            return None

        max_condition_item = same_category_list[0]

        for item in same_category_list:
            if item.condition > max_condition_item.condition:
                max_condition_item = item
        
        return max_condition_item


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        other_best_item = other_vendor.get_best_by_category(my_priority)
        
        if not my_best_item or not other_best_item:
            return False

        return self.swap_items(other_vendor, my_best_item, other_best_item)


    def display_inventory(self, category = ""):
        n = 1
        if self.inventory == []:
            print("No inventory to display.")
        elif category!="" and self.get_by_category(category) == []:
            print("No inventory to display.")
        
        if category == "":
            for item in self.inventory:
                print(f"{n}. {item. __str__()}")
                n += 1
        
        for item in self.get_by_category(category):
            print(f"{n}. {item. __str__()}")
            n += 1


    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_id_item = self.get_by_id(my_item_id)
        other_id_item = other_vendor.get_by_id(their_item_id)

        if my_id_item == None or other_id_item == None:
            return False
    
        return self.swap_items(other_vendor, my_id_item, other_id_item)


    def choose_and_swap_items(self, other_vendor, category = ""):
        self.display_inventory(category)
        other_vendor.display_inventory(category)

        flag = True
        self_id = 0
        other_id = 0
        
        while flag:
            self_id = int(input("self_item_id: "))
            other_id = int(input("other_item_id: "))
            if self_id and other_id:
                flag = False
        
        result = self.swap_by_id(other_vendor, self_id, other_id)
        return result

    # working on Optional Enhancements in new branch and doesn't finish
    # will submit it later. Thank you!