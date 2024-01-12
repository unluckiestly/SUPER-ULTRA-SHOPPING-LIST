import csv
import os

class ShoppingListManager:
    def __init__(self):
        self.shopping_list = []
        self.shopping_lists = []
        self.current_list = 0
        self.list_count = 0
        self.total_cost = 0

    def print_shop_menu(self):
        print("Hello, you are in shopping list: ")
        print("1. Add new item list")
        print("2. Remove item list")
        print("3. Show all item lists")
        print("4. Change current list")
        print("-----------------------------")
        try:
            print(f"Current list: {self.shopping_lists[self.current_list]["list_name"]}")
        except IndexError:
            print(f"Current list: {self.current_list}")
        print("5. Add new item to list")
        print("6. Remove item from list")
        print("7. Reveal all items in list")

    def add_list(self, list_name, list, item_count = 0):
        list = {"list_name": list_name, "list": list, "item_count": item_count}
        self.shopping_lists.append(list)
        self.list_count += 1

    def remove_list(self, index):
        del self.shopping_lists[index]
        self.list_count -= 1

    def add_item(self, name, price, quantity):
        item = {"name": name, "price": int(price), "quantity": int(quantity)}
        self.shopping_lists[self.current_list]["list"].append(item)
        self.shopping_lists[self.current_list]["item_count"] += 1
        print(f"ASDASDASD {self.shopping_lists[self.current_list]["item_count"]}")

    def remove_item(self, index):
        del self.shopping_lists[self.current_list]["list"][index]
        self.shopping_lists[self.current_list]["item_count"] -= 1
        
    def calculate_total_cost(self):
        if self.shopping_lists:
            try:
                self.total_cost = sum(int(item["price"]) * int(item["quantity"]) for item in self.shopping_lists[self.current_list]["list"])
            except ValueError:
                print("invalid price")

    def export_to_txt(self, row):
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

        file_path = "C:\\Users\\kiril\\OneDrive\\Desktop\\shopping.list.txt"
        try:
            with open(file_path, 'w') as file:
                file.write(row)
            print(f"file succesfully created.")
        except Exception as e:
            print(f"error occured while creating file: {e}")



manager = ShoppingListManager()

def shopping_list():
    manager.print_shop_menu()
    a = int(input("Enter your choice: "))

    if a == 1: # add a new list
        list_name, list = input("What will be list name?: "), []
        manager.add_list(list_name, list)
        print(f"ASDASDASD {manager.shopping_lists[manager.current_list]["item_count"]}")
    elif a == 2: # remove active item list
        manager.remove_list(manager.current_list)
    elif a == 3: # show all item lists
        print(manager.shopping_lists)
    elif a == 4: # change active item list
        for i in range(len(manager.shopping_lists)):
            print(f"{i + 1}. {manager.shopping_lists[i]["list_name"]}")
        manager.current_list = int(input("Enter number of list: ")) - 1
    elif a == 5: # add item to list
        try:
            if len(manager.shopping_lists) != 0:
                name, price, quantity = input("enter item name: "), input("enter item price: "), input("enter item quantity: ")
                manager.add_item(name, price, quantity)
            else:
                print("You have not any lists.")
        except TypeError:
            print("An error occurred while adding the list")
    elif a == 6: # remove item from list
        index = int(input("enter item index: "))
        manager.remove_item(index)
    elif a == 7: # reveal all items in list
        for i in manager.shopping_lists[manager.current_list]["list"]:
            print(f"Name: {i["name"]}, Price: {i["price"]}, Quantity: {i["quantity"]}\n") 
        print(manager.calculate_total_cost())

if __name__ == '__main__':
    while True:
        shopping_list()
