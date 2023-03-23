import tkinter as tk
from tkinter import ttk


class Item:
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description

# サンプルデータ
items = [
    Item("Example 1", "https://example.com/1", "This is an example link 1."),
    Item("Example 2", "https://example.com/2", "This is an example link 2."),
    Item("Example 3", "https://example.com/3", "This is an example link 3."),
]


def add_item():
    title = title_entry.get()
    link = link_entry.get()
    description = desc_entry.get()

    items.append(Item(title, link, description))
    update_list()


def update_list():
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item.title)


def on_listbox_select(event):
    index = listbox.curselection()[0]
    selected_item = items[index]

    title_entry.delete(0, tk.END)
    title_entry.insert(0, selected_item.title)

    link_entry.delete(0, tk.END)
    link_entry.insert(0, selected_item.link)

    desc_entry.delete(0, tk.END)
    desc_entry.insert(0, selected_item.description)


root = tk.Tk()
root.title("List Editor")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

title_label = ttk.Label(frame, text="Title:")
title_label.grid(column=0, row=0, sticky=tk.W)
title_entry = ttk.Entry(frame)
title_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

link_label = ttk.Label(frame, text="Link:")
link_label.grid(column=0, row=1, sticky=tk.W)
link_entry = ttk.Entry(frame)
link_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

desc_label = ttk.Label(frame, text="Description:")
desc_label.grid(column=0, row=2, sticky=tk.W)
desc_entry = ttk.Entry(frame)
desc_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

add_button = ttk.Button(frame, text="Add/Update Item", command=add_item)
add_button.grid(column=1, row=3, sticky=tk.E)

listbox = tk.Listbox(root)
listbox.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
listbox.bind("<<ListboxSelect>>", on_listbox_select)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

update_list()
root.mainloop()
