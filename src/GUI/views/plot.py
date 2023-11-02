import tkinter

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from reliavision.gui.views.common import ViewBase


class Plot(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, parent=None, width=800, height=600):
        tkinter.Frame.__init__(self, parent)
        ViewBase.__init__(
            self,
            model,
            controller,
            "plot",
            parent=parent,
            width=width,
            height=height,
        )

    def create_plot(self, parent, width, height, key):
        fig = Figure()
        ax = fig.add_subplot(111)

        row = len(self.plots.keys()) + 1
        column = 0

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.get_tk_widget().config(width=width, height=height)
        canvas.get_tk_widget().grid(row=row, column=column, sticky="nsew")

        self.plots[key] = {"fig": fig, "ax": ax, "canvas": canvas}

        self.add_navbar(parent, key, row=row + 1, column=column)

    def add_navbar(self, parent, key, row=0, column=0):

        toolbar_frame = tkinter.Frame(parent)
        matplotlib.backends.backend_tkagg.NavigationToolbar2Tk(
            self.plots[key]["canvas"], toolbar_frame
        )

        toolbar_frame.grid(row=row, column=column, sticky="sew")

    def _setupView(self, model, controller, **kwargs):
        self._parent = kwargs["parent"]
        self._width = kwargs["width"]
        self._height = kwargs["height"]

    def init_plot(self, master):
        self._fig = Figure()
        self.ax = self._fig.add_subplot(111)
        self._fig.subplots_adjust(left=0.15)

        self.ax.plot([], [], label="1")

        self.ax.grid()

        self.canvas = FigureCanvasTkAgg(self._fig, master=master)

        self._toolbar_frame = tkinter.Frame(master)
        matplotlib.backends.backend_tkagg.NavigationToolbar2Tk(
            self.canvas, self._toolbar_frame
        )

        self.canvas.get_tk_widget().config(width=self._width, height=self._height)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=4, sticky="news")
        self._toolbar_frame.grid(row=6, column=0, columnspan=4, sticky="sew")

        master.columnconfigure(1, weight=1)

    def update_plot(self, devices, values, fom_name):

        self.ax.clear()

        self.ax.set_title(fom_name)

        self.ax.barh(
            np.linspace(0, len(values) - 1, len(values)), values, tick_label=devices
        )
        self.ax.set_xlabel("degradation [%]")
        self.ax.set_ylabel("device name")
        self.ax.grid()
        self.ax.set_axisbelow(True)
        # self._fig.tight_layout()
        self.canvas.draw()

    def setup_controller(self):
        pass

    def setup_plot_menu(self, fom_names):
        window = self._parent

        self._variable = tkinter.StringVar(window)
        self._variable.set(fom_names[0])  # default value

        self._menu = tkinter.OptionMenu(
            self._parent,
            self._variable,
            *fom_names,
            command=self._controller.get_callback(
                "get_device_aging", id=self._name + "_ageing", fom=self._variable
            )
        )

        self._menu.grid(row=0, column=0, sticky="swe")

    def update(self):
        state = self._model.getState()

        # set menu
        if "max_foms" in list(state.keys()):
            self.init_plot(self._parent)

            self.setup_plot_menu(state["max_foms"]["fom"])

            data = state["max_foms"]["data"]
            self.update_plot(data["devices"], data["values"], data["fom"])

        if self._name + "_ageing" in list(state.keys()):
            data = state[self._name + "_ageing"]

            self.update_plot(data["devices"], data["values"], data["fom"])
            # self.create_plot(self._parent, self._width, self._height, fom_name)
