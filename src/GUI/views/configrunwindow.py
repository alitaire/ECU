import tkinter
from tkinter import messagebox

from reliavision.gui.views.common import ViewBase


class ConfigRunWindow(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, master):
        tkinter.Frame.__init__(self, master)
        ViewBase.__init__(self, model, controller, "ConfigRunWindow", parent=master)

    def _setupView(self, model, controller, **kwargs):
        self._window = self.winfo_toplevel()
        self._window.title("Simulation options")

        self._window.protocol("WM_DELETE_WINDOW", self.__on_closing)

        text = [
            " ",
            "    This function is currently not available :(    ",
            " ",
        ]

        for i, text_label in enumerate(text):
            tkinter.Label(self._window, text=text_label).grid(row=i, column=0, sticky="nw")

    def _setupView_2(self, model, controller, **kwargs):
        self._window = self.winfo_toplevel()

        self._window.protocol("WM_DELETE_WINDOW", self.__on_closing)

        # Lifetime
        tkinter.Label(self._window, text="Target Lifetime ", width=20).grid(
            row=0, column=0
        )
        tkinter.Entry(self._window).grid(row=0, column=1)
        tkinter.Label(self._window, text="yrs").grid(row=0, column=2)

        # Temperature
        tkinter.Label(self._window, text="Temperature ", width=20).grid(row=1, column=0)
        tkinter.Entry(self._window).grid(row=1, column=1)
        tkinter.Label(self._window, text="°C").grid(row=1, column=2)

        # Strss Period
        tkinter.Label(self._window, text="Stress Period ", width=20).grid(
            row=2, column=0
        )
        tkinter.Entry(self._window).grid(row=2, column=1)
        tkinter.Label(self._window, text="s").grid(row=2, column=2)

        # Voltage
        tkinter.Label(self._window, text="Vg ", width=20).grid(row=3, column=0)
        tkinter.Entry(self._window).grid(row=3, column=1)
        tkinter.Label(self._window, text="V").grid(row=3, column=2)

        tkinter.Label(self._window, text="Vd ", width=20).grid(row=4, column=0)
        tkinter.Entry(self._window).grid(row=4, column=1)
        tkinter.Label(self._window, text="V").grid(row=4, column=2)

        tkinter.Label(self._window, text="Vs ", width=20).grid(row=5, column=0)
        tkinter.Entry(self._window).grid(row=5, column=1)
        tkinter.Label(self._window, text="V").grid(row=5, column=2)

        self.__okButton = tkinter.Button(self._window, text="OK", width=25)

        self.__okButton.grid(row=6, column=0, sticky="swe")

        self._window.title("Configure Ageing Simulation")

    def __on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self._window.destroy()

    def setup_controller(self):
        self.__okButton.configure(
            command=self._controller.get_callback("quit_window", name=self.get_name())
        )

    def update(self):
        self._state = self._model.getState()
        # print(self._name)
        # print(self._state)
