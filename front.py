from tkinter import *
from back import *

def bubble_sort(dict_list):
    n = len(dict_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if dict_list[j]["price"] > dict_list[j+1]["price"]:
                dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]

m = Tk()
m.geometry("1046x713")
m.resizable(False,False)
m.title("Shopping list")

canvas = Canvas(m, width= 1046, height= 713)

canvas.create_text(24, 70, text="name", fill="black", font="Arial 10")
canvas.create_text(22, 95, text="price", fill="black", font="Arial 10")
canvas.create_text(30, 120, text="quantity", fill="black", font="Arial 10")

canvas.create_text(690, 25, text=f"Total cost: {manager.total_cost}", fill="black", font="Arial 10", tag="a")

entry = Entry(m, width=36)
entry.place(x=65, y=225)

entry_price = Entry(m, width=36)
entry_price.place(x=65, y=250)

entry_quantity = Entry(m, width=36)
entry_quantity.place(x=65, y=275)

entry_list = Entry(m, width=36)
entry_list.place(x=45, y=425)

item_list = Listbox(m, width=70)
lists = Listbox(m, width=20)

def draw_lists():
    item_list.delete(0,END)
    lists.delete(0,END)
    canvas.delete("a")
    manager.calculate_total_cost()
    canvas.create_text(690, 25, text=f"Total cost: {manager.total_cost}", fill="black", font="Arial 10", tag="a")
    for i in range(manager.shopping_lists[manager.current_list]["item_count"]):
        item_list.insert(i, f"{manager.shopping_lists[manager.current_list]["list"][i]["name"]} | price: {manager.shopping_lists[manager.current_list]["list"][i]["price"]} | quantity: {manager.shopping_lists[manager.current_list]["list"][i]["quantity"]}")

    for i in range(manager.list_count):
        lists.insert(i, manager.shopping_lists[i]["list_name"])

def add_item_wrapper():
    if entry.get() == "" or entry_price.get() == "" or entry_quantity.get() == "":
        return
    try:   
        manager.add_item(entry.get(), entry_price.get(), entry_quantity.get())
    except ValueError:
        print("invalid value")
    draw_lists()

def delete_item_wrapper():
    if item_list.curselection():
        manager.remove_item(item_list.curselection()[0])
    draw_lists()

def add_list_wrapper():
    if entry_list.get() == "":
        return
    
    manager.add_list(entry_list.get(), [])
    draw_lists()

def delete_list_wrapper():
    if lists.curselection():
        manager.remove_list(lists.curselection()[0])
    draw_lists()
    
def select_list():
    if lists.curselection():
        manager.current_list = lists.curselection()[0]
    draw_lists()

def bubble_sort_wrapper():
    bubble_sort(manager.shopping_lists[manager.current_list]["list"])
    print(manager.shopping_lists[manager.current_list]["list"])
    draw_lists()
    
def export_wrapper():
    row = ""
    for i in range(manager.shopping_lists[manager.current_list]["item_count"]):
        row += f"{manager.shopping_lists[manager.current_list]["list"][i]["name"]} | price: {manager.shopping_lists[manager.current_list]["list"][i]["price"]} | quantity: {manager.shopping_lists[manager.current_list]["list"][i]["quantity"]}\n"
    
    manager.export_to_txt(row)

add = Button(m, text="Add item", width=30, height=3, command=add_item_wrapper)
add.place(x=45, y=47)

delete = Button(m, text="Delete item", width=30, height=3, command=delete_item_wrapper)
delete.place(x=45, y=128)

sort = Button(m, text = "Sort items by price", width=15, height=3, command=bubble_sort_wrapper)
sort.place(x=311, y=170)

add_list = Button(m, text="Add new list", width=30, height=3, command=add_list_wrapper)
add_list.place(x=45, y=460)

delete_list = Button(m, text="Remove list", width=30, height=3, command=delete_list_wrapper)
delete_list.place(x=45, y=535)

swap_list = Button(m, text="Select list", width=30, height=3, command=select_list)
swap_list.place(x=45, y=610)

export = Button(m, text="Export to txt file", width=25, height=3, command=export_wrapper)
export.place(x=800, y=600)

item_list.pack()
lists.place(x=750, y=0)
canvas.pack()


m.mainloop()


