'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    '''
    classdocs
    '''

    PAD = 10

    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
        ]

    def __init__(self, controller):
        super().__init__()

        self.title('ECU')

        self.controller = controller

        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()


    def main(self):
        print("In main of view")
        self.mainloop()


    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)


    def _make_entry(self):
        ent = ttk.Entry(self.main_frame, justify='right', textvariable=self.value_var)
        ent.pack(fill='x')


    def _make_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        frame = ttk.Frame(outer_frame)
        frame.pack()

        for idx, caption in enumerate(self.button_captions):
            if (idx % self.MAX_BUTTONS_PER_ROW) == 0:
                frame = ttk.Frame(outer_frame)
                frame.pack()

            btn = ttk.Button(frame, text=caption,
                             command=(lambda button=caption: self.controller.on_button_click(button)))
            btn.pack(side='left')

