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
        self.port = "COM3"
        self.baudrate = "115200"

        self._setup_main_frame()
        self._setup_com_type()
        self._setup_com_settings()


    def _setup_main_frame(self):
        self._main_frame = ttk.Labelframe(self, text="Communication Settings", borderwidth=5, relief='solid')

        self._com_type = ttk.Labelframe(self._main_frame, text="Connection Type", borderwidth=5, relief='solid')
        self._com_settings = ttk.Labelframe(self._main_frame, text="Connection Settings", borderwidth=5, relief='solid')
        self.connect_btn = ttk.Button(self._main_frame, text="Connect", command=self.callback_connect)
        self.disconnect_btn = ttk.Button(self._main_frame, text="Disconnect", command=self.callback_disconnect)
        self.connect_stat = tk.Label(self._main_frame, text="Not Connected")

        self._main_frame.pack()
        self._com_type.pack()
        self._com_settings.pack()
        self.connect_btn.pack()
        self.disconnect_btn.pack()
        self.connect_stat.pack()


    def _setup_com_type(self):
        self.selected_type = tk.StringVar()
        type_cb = ttk.Combobox(self._com_type, textvariable=self.selected_type)
        type_cb['value'] = ('USB-OTG', 'UART')
        type_cb['state'] = 'readonly'
        type_cb.set(type_cb['value'][1])
        type_cb.pack()


    def _setup_com_settings(self):
        self._setup_setting(self._com_settings, "Port", self.port)
        self._setup_setting(self._com_settings, "Baud rate", self.baudrate)


    def _setup_setting(self, parent, label_text, var):
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text=label_text)
        entry = ttk.Entry(frame, textvariable=var)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        frame.pack(padx=5, pady=5)


    def callback_connect(self):
        if self.baudrate is None or self.port is None:
            print("Error: You should provide arguments for baudrate & port before trying to connect")
        else:
            print(f"Port : {self.port}")
            print(f"Baud rate : {self.baudrate}")
            self._controller.connect_uart(self.port, self.baudrate)


    def callback_disconnect(self):
            self._controller.disconnect_uart()


    def update(self):
        state = self._model.getState()

        if "Com" in state.keys():
            print("Update Communication")
            self.connect_stat.configure(text=state["Com"])
            self.connect_stat.bell()

