'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import tkinter as tk
from views import ViewInterface

class Voyant(tk.Canvas, ViewInterface):
    '''
    classdocs
    '''

    def __init__(self, parent, model, controller, name, color="orange", size=30, border=2):
        super().__init__(parent, width=size, height=size)

        self._model = model
        self._controller = controller
        self._name = name

        self.size = size
        self.border = border

        self.blink_color = color
        self.base_color = "white"
        self.color = self.base_color
        self.isblinked = False

        self.draw()


    def draw(self):
        self.delete("all")
        self.create_oval(self.border, self.border, self.size, self.size, fill=self.color, outline="black", width=2)


    def blink(self):
        if self.isblinked:
            self.color = self.base_color
        else:
            self.color = self.blink_color

        self.draw_led()
        self.isblinked = not self.isblinked


    def update(self):
        state = self._model.getState()

        if self._name in state.keys():
            print(f"Update {self._name}")
            self.blink()