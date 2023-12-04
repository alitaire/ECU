'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import sys
import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from views import ViewInterface
from views import Counter
from views import Communication


class MainWindow(tk.Tk, ViewInterface):
    '''
    classdocs
    '''

    def __init__(self, controller, model, width=1500, height=900):
        super().__init__()
        self._controller = controller
        self._model = model

        self.title('ECU')
        self._width = width
        self._height = height

        self._setupView()


    def _setupView(self):
        self.geometry(f"{self._width}x{self._height}")
        self.mainlayout = ttk.Frame(self, relief="sunken")
        self.inlayout = ttk.Frame(self.mainlayout, relief="sunken")
        self.outlayout = ttk.Frame(self.mainlayout, relief="sunken")

        self.mainlayout.pack(padx=10, pady=10)
        self.outlayout.grid(column=0, row=0, padx=10, pady=10)
        self.inlayout.grid(column=1, row=0, padx=10, pady=10)

        self._setup_MenuBar()
        self._setup_Counters()
        self._setup_Buttons()


    def _setup_MenuBar(self):
        menu_bar = tk.Menu(self)

        menu_file = tk.Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", command=self.do_something)
        menu_file.add_command(label="Open", command=self.open_file)
        menu_file.add_command(label="Save", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        menu_edit = tk.Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Undo", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Copy", command=self.do_something)
        menu_edit.add_command(label="Cut", command=self.do_something)
        menu_edit.add_command(label="Paste", command=self.do_something)
        menu_bar.add_cascade(label="Edit", menu=menu_edit)

        menu_connect = tk.Menu(menu_bar, tearoff=0)
        menu_connect.add_command(label="Test", command=self.open_com)
        menu_bar.add_cascade(label="Connect", menu=menu_connect)

        menu_tune = tk.Menu(menu_bar, tearoff=0)
        menu_tune.add_command(label="Ohhh Yeaaah", command=self.do_something)
        menu_bar.add_cascade(label="Tune", menu=menu_tune)

        menu_help = tk.Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About", command=self.do_about)
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.config(menu=menu_bar)


    def _setup_Counters(self):
        # Affichage Throttle
        self.throttle = Counter(self.inlayout, controller=self._controller, model=self._model,
                                name="Throttle", unit="%", max_unit=100)
        self._model.attach(self.throttle)
        self.throttle.grid(column=0, row=0, padx=10, pady=10)

        # Affichage Engine Speed
        self.speed = Counter(self.inlayout, controller=self._controller, model=self._model,
                             name="Speed", unit="tr/min x 100", max_unit=80)
        self._model.attach(self.speed)
        self.speed.grid(column=0, row=1, padx=10, pady=10)

        # Affichage Air intake temperature
        self.airtemp = Counter(self.inlayout, controller=self._controller, model=self._model,
                               name="AirTemp", unit="Air T°C", min_unit=-30, max_unit=90)
        self._model.attach(self.airtemp)
        self.airtemp.grid(column=1, row=0, padx=10, pady=10)

        # Affichage Coolant temperature
        self.cooltemp = Counter(self.inlayout, controller=self._controller, model=self._model,
                                name="CoolTemp", unit="Coolant T°C", min_unit=-30, max_unit=150)
        self._model.attach(self.cooltemp)
        self.cooltemp.grid(column=1, row=1, padx=10, pady=10)

        # Ajout d'autres mesures


    def _setup_Buttons(self):
        for i in range(0, 9):
            tmp_btn = tk.Button(self.outlayout, height=10, width=20)
            tmp_btn.config(text=f"Btn{i}")
            tmp_btn.grid(column=i%3, row=i//3, padx=10, pady=20)
        '''
        self.clutch = tk.Button(self.outlayout)
        self.clutch.config(text="Clutch")
        self.clutch.grid(column=0, row=0, padx=10, pady=10)

        self.brake = tk.Button(self.outlayout)
        self.brake.config(text="Brake")
        self.brake.grid(column=1, row=0, padx=10, pady=10)
        '''

    def open_file(self):
        file = askopenfilename(title="Choose the file to open",
                               filetypes=[("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")])
        print(file)


    def open_com(self):
        com = Communication(controller=self._controller, model=self._model)
        com.mainloop()

    def do_something(self):
        print("Menu clicked")
        self._controller.incr()


    def do_about(self):
        messagebox.showinfo("My title", "My message")


    def update(self):
        state = self._model.getState()

        if "MainWindow" in state.keys():
            print("Update MainWindow")

