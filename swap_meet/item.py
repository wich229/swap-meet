import uuid


class Item:

    def __init__(self, id = None, condition = 0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
    

    def get_category(self):
        return self.__class__.__name__


    def condition_description(self):
        level_explained = {
            0 : "no explained",
            1 : "heavily used",
            2 : "refurbished",
            3 : "well maintain",
            4 : "sample item",
            5 : "brand new"
        }
        return level_explained[int(self.condition)]
    

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"
   
