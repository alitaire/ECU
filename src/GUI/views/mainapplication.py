'''
    Created on Nov 05, 2023

    @author: Bastien DELAUNAY
'''


import sys
import math
import tkinter as tk
from tkinter import ttk
from src.GUI.views.interface import ViewInterface
from src.GUI.views.afficheur import Counter


class MainWindow(tk.Tk, ViewInterface):
    '''
    classdocs
    '''

    def __init__(self, controller, model, width=1080, height=720):
        super().__init__()
        self._controller = controller
        self._model = model

        self.title('ECU')
        self._width = width
        self._height = height

        self.speedView = Counter(self, controller=self._controller, model=self._model, name="Speed")
        self._model.attach(self.speedView)

        self.tempView = Counter(self, controller=self._controller, model=self._model, name="Temp")
        self._model.attach(self.tempView)

        self._setupView()


    def _setupView(self):
        self.speedView.maxUnit = 100
        self.speedView.unit = "%"
        self.speedView.pack()

        self.tempView.maxUnit = 150
        self.tempView.unit = "°C"
        self.speedView.pack()


    def update(self):
        state = self._model.getState()

        if "MainWindow" in state.keys():
            print("Update MainWindow")

