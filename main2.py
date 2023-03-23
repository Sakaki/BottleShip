import tkinter as tk
from tkinter import simpledialog, messagebox


class StringListEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("String List Editor")
        self.geometry("400x400")

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_item)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit", command=self.edit_item)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_item)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_item(self):
        new_item = simpledialog.askstring("Add Item", "Enter new item:")
        if new_item:
            self.listbox.insert(tk.END, new_item)

    def edit_item(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No item selected")
            return

        old_item = self.listbox.get(selected_index)
        new_item = simpledialog.askstring("Edit Item", "Edit item:", initialvalue=old_item)
        if new_item:
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, new_item)

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No item selected")
            return

        self.listbox.delete(selected_index)


if __name__ == "__main__":
    app = StringListEditor()
    app.mainloop()
