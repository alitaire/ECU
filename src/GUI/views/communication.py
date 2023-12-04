'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import tkinter as tk
from tkinter import ttk
from views import ViewInterface


class Communication(tk.Tk, ViewInterface):
    '''
    classdocs
    '''

    def __init__(self, controller, model):
        super().__init__()

        self.title('Communication')

        self._controller = controller
        self._model = model

        self._setup_main_frame()
        self._setup_com_type()
        self._setup_com_settings()


    def _setup_main_frame(self):
        self._main_frame = ttk.Labelframe(self, text="Communication Settings", borderwidth=5, relief='solid')

        self._com_type = ttk.Labelframe(self._main_frame, text="Connection Type", borderwidth=5, relief='solid')
        self._com_settings = ttk.Labelframe(self._main_frame, text="Connection Settings", borderwidth=5, relief='solid')
        self._test_frame = ttk.Frame(self._main_frame)

        test_label = ttk.Label(self._test_frame, text="Not tested")
        test_btn = ttk.Button(self._test_frame, text="Test Port")
        detect_btn = ttk.Button(self._test_frame, text="Detect")

        test_label.grid(row=0, column=0)
        test_btn.grid(row=0, column=1)
        detect_btn.grid(row=0, column=2)

        self._main_frame.pack()
        self._com_type.pack()
        self._com_settings.pack()
        self._test_frame.pack()


    def _setup_com_type(self):
        selected_type = tk.StringVar()
        type_cb = ttk.Combobox(self._com_type, textvariable=selected_type)
        type_cb['value'] = ('RS232', 'UART')
        type_cb['state'] = 'readonly'
        type_cb.set(type_cb['value'][1])
        type_cb.pack()

    def _setup_com_settings(self):
        pass


    def update(self):
        state = self._model.getState()

        if "Com" in state.keys():
            print("Update Communication")

