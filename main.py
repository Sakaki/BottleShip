import tkinter as tk
from tkinter import messagebox


class LinkInfo:
    def __init__(self, link, title, subtitle, description):
        self.link = link
        self.title = title
        self.subtitle = subtitle
        self.description = description


class App:
    def __init__(self, master):
        self.master = master
        self.link_info_list = []

        self.link_entry = tk.Entry(master, width=50)
        self.link_entry.grid(row=0, column=1)
        self.title_entry = tk.Entry(master, width=50)
        self.title_entry.grid(row=1, column=1)
        self.subtitle_entry = tk.Entry(master, width=50)
        self.subtitle_entry.grid(row=2, column=1)
        self.description_entry = tk.Entry(master, width=50)
        self.description_entry.grid(row=3, column=1)

        self.link_label = tk.Label(master, text="Link")
        self.link_label.grid(row=0, column=0)
        self.title_label = tk.Label(master, text="Title")
        self.title_label.grid(row=1, column=0)
        self.subtitle_label = tk.Label(master, text="Subtitle")
        self.subtitle_label.grid(row=2, column=0)
        self.description_label = tk.Label(master, text="Description")
        self.description_label.grid(row=3, column=0)

        self.add_button = tk.Button(master, text="Add", command=self.add_link_info)
        self.add_button.grid(row=4, column=1)

    def add_link_info(self):
        link = self.link_entry.get()
        title = self.title_entry.get()
        subtitle = self.subtitle_entry.get()
        description = self.description_entry.get()

        if not link or not title or not subtitle or not description:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        link_info = LinkInfo(link, title, subtitle, description)
        self.link_info_list.append(link_info)

        self.link_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.subtitle_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    root.title("Link Info Editor")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
