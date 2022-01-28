

class ShoppingList():
    def __init__(self, list, item):
        self.item = item
        self.list = []

    def add(self):
        if self.item.isalpha():
            self.list.append(self.item)
            return self.list.append(self.item)

    def remove(self):
        return self.list.remove(self.item)

    def show(self):
        print(f'here is your current list {self.list}')

x = ShoppingList('list', 'item')


class Prints():
    def __init__(self, list, item):
        self.item = item
        self.list = list

    def added(self):
        print(f'{self.item} has been added to the list.')

    def current(self):
        print(f'Here is your current list: {self.list}')    

    def final(self):
        print(f'Here is your final list: {self.list}')

    def not_found(self):
        print(f'{self.item} not found in list.')


    def deleted(self):
        print(f'{self.item} has been deleted from your list. Here is your current list: {self.list}')

    def invalid(self):
        print('invalid input, try again')

y = Prints('list', 'item')

def create_list():
    list = []
    while True:
        item = input('Tell me what you want to add to your shopping list. ')
        if item.isalpha():
            x.add
            y.added
            y.current
        else:
            y.invalid
            continue
        
        active = True
        while active:
            decision = input('Enter 1 to add more items, 0 to delete an item, or quit to exit. ').lower()
            if decision == '1':
                break
            elif decision == '0':
                deleted = input(f'Please tell me the item you want to delete: {list} ')
                if deleted in list:
                    x.remove
                    y.deleted
                else:
                    y.not_found
            elif decision == 'quit':
                y.final
                return
            else:
                y.invalid


create_list()

   