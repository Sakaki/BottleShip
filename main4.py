import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import json
from pathlib import Path
from Item import Form

keys = [
    "twitterUrl",
    "pixivUrl",
    "completed",
    "rough",
    "line",
    "timeLapse",
    "title",
    "subtitle",
    "description",
    "iconColor"
]


class ListEditor:
    def __init__(self, master):
        self.master = master
        self.items = []

        self.forms = []
        for row, key in enumerate(keys):
            label = ttk.Label(self.master, text=f'{key}:')
            label.grid(column=0, row=row, sticky=tk.W)
            if key == 'description':
                entry = ScrolledText(self.master, width=100, height=5)
            else:
                entry = ttk.Entry(self.master, width=100)
            entry.grid(column=1, row=row, sticky=(tk.W, tk.E))
            self.forms.append(Form(key, label, entry))

        add_button = ttk.Button(self.master, text="Add/Update Item", command=self.add_or_update_item)
        add_button.grid(column=1, row=len(keys) + 1, sticky=tk.E)

        clear_button = ttk.Button(self.master, text="Clear", command=self.clear_form)
        clear_button.grid(column=1, row=len(keys) + 2, sticky=tk.E)

        import_button = ttk.Button(self.master, text="Import", command=self.import_list)
        import_button.grid(column=1, row=len(keys) + 3, sticky=tk.E)

        export_button = ttk.Button(self.master, text="Export", command=self.export_list)
        export_button.grid(column=1, row=len(keys) + 4, sticky=tk.E)

        listbox = tk.Listbox(root, width=50)
        listbox.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.listbox = listbox

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item.get('title'))

    def clear_form(self):
        for index in range(len(self.forms)):
            self.forms[index].update('')
        self.update_list()

    def add_or_update_item(self):
        to_add = {}
        for form in self.forms:
            to_add[form.key] = form.value()
        index = -1
        for temp, item in enumerate(self.items):
            if item['title'] == to_add['title']:
                index = temp
                break
        if index == -1:
            self.items.insert(0, to_add)
            self.clear_form()
        else:
            self.items[index] = to_add
        self.update_list()

    def on_listbox_select(self, event):
        try:
            index = self.listbox.curselection()[0]
        except IndexError:
            return
        selected_item = self.items[index]
        for form in self.forms:
            form.update(selected_item[form.key])
        self.update_list()

    @staticmethod
    def gen_item(items):
        return {
            "twitterUrl": items[0]['entry'].get(),
            "pixivUrl": items[1]['entry'].get(),
            "completed": items[2]['entry'].get(),
            "rough": items[3]['entry'].get(),
            "line": items[4]['entry'].get(),
            "timeLapse": items[5]['entry'].get(),
            "title": items[6]['entry'].get(),
            "subtitle": items[7]['entry'].get(),
            "description": items[8]['entry'].get(),
            "iconColor": items[9]['entry'].get()
        }

    def add_item_to_list(self, items):
        self.items.append(self.gen_item(items))
        self.refresh_listbox()

    def remove_item(self):
        selection = self.listbox.curselection()
        if selection:
            self.items.pop(selection[0])
            self.refresh_listbox()

    def edit_item(self):
        selection = self.listbox.curselection()
        if selection:
            item = self.items[selection[0]]
            print(item)
            edit_window = tk.Toplevel(self.master)
            items = []

            for key in keys:
                label = tk.Label(edit_window, text=key)
                label.pack()
                entry = tk.Entry(edit_window)
                entry.insert(0, item.get(key))
                entry.pack()
                items.append({
                    "label": label,
                    "entry": entry
                })

            edit_button = tk.Button(
                edit_window,
                text="Save",
                command=lambda: self.save_edited_item(
                    selection[0],
                    items
                )
            )
            edit_button.pack()

    def save_edited_item(self, index, items):
        self.items[index] = self.gen_item(items)
        self.refresh_listbox()

    def export_list(self):
        file_path = Path('test.json', encodings='utf-8')
        to_save = []
        for item in self.items:
            to_save.append({
                "link": {
                    "twitterUrl": item['twitterUrl'],
                    "pixivUrl": item['pixivUrl']
                },
                "imageUrls": {
                    "completed": item['completed'],
                    "rough": item['rough'],
                    "line": item['line'],
                    "timeLapse": item['timeLapse']
                },
                "title": item['title'],
                "subtitle": item['subtitle'],
                "description": item['description'],
                "props": {
                    "iconColor": item['iconColor']
                }
            })
        file_path.write_text(json.dumps(to_save, indent=4, ensure_ascii=False), encoding='utf-8')

    def import_list(self):
        file_path = Path('test.json', encodings='utf-8')
        import_json = json.loads(file_path.read_text(encoding='utf-8'))
        items = []
        for item in import_json:
            items.append({
                "twitterUrl": item['link']['twitterUrl'],
                "pixivUrl": item['link']['pixivUrl'],
                "completed": item['imageUrls']['completed'],
                "rough": item['imageUrls']['rough'],
                "line": item['imageUrls']['line'],
                "timeLapse": item['imageUrls']['timeLapse'],
                "title": item['title'],
                "subtitle": item['subtitle'],
                "description": item['description'],
                "iconColor": item['props']['iconColor']
            })
        self.items = items
        self.update_list()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, f"{item['title']} - {item['subtitle']}")


if __name__ == "__main__":
    root = tk.Tk()
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    app = ListEditor(frame)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
