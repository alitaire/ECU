import os
import tkinter as tk
from tkinter import ttk

def populate_tree(tree, node):
    if tree.set(node, "type") != 'directory':
        return

    path = tree.set(node, "fullpath")
    tree.delete(*tree.get_children(node))

    parent = tree.parent(node)
    special_dirs = [".", ".."]

    for p in os.listdir(path):
        ptype = None
        p = os.path.join(path, p).replace('\\', '/')
        if os.path.isdir(p): ptype = "directory"
        elif os.path.isfile(p): ptype = "file"

        fname = os.path.split(p)[1]
        id = tree.insert(node, "end", text=fname, values=[p, ptype])

        if ptype == 'directory':
            if fname not in special_dirs:
                tree.insert(id, 0, text="dummy")

def update_tree(event):
    tree = event.widget
    populate_tree(tree, tree.focus())

def on_open(event):
    tree = event.widget
    item = tree.focus()
    if tree.set(item, "type") == 'file':
        file_path = tree.set(item, "fullpath")
        print("Fichier sélectionné :", file_path)

root = tk.Tk()
root.title("Explorateur de répertoire")

tree = ttk.Treeview(root)
tree["columns"] = ("fullpath", "type")
tree.column("#0", width=150, minwidth=50, stretch=tk.NO)
tree.column("fullpath", width=0, stretch=tk.NO)
tree.column("type", width=50, minwidth=50, stretch=tk.NO)

tree.heading("#0", text="Nom", anchor=tk.W)
tree.heading("type", text="Type", anchor=tk.W)

populate_tree(tree, "")

tree.bind("<Double-1>", on_open)
tree.bind("<<TreeviewOpen>>", update_tree)

tree.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
