import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Form:
    def __init__(self, key, label, entry):
        self.key = key
        self.label = label
        self.entry = entry

    def update(self, text):
        if type(self.entry) == ScrolledText:
            self.entry.delete(1.0, tk.END)
            self.entry.insert(tk.INSERT, text)
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, text)

    def value(self):
        if type(self.entry) == ScrolledText:
            return self.entry.get("1.0", tk.END).strip('\n')
        else:
            return self.entry.get()
