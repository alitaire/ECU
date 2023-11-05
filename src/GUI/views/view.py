'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title('ECU')


    def main(self):
        print("In main of view")
        self.mainloop()
