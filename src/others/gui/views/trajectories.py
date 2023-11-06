import tkinter

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from reliavision.gui.views.common import ViewBase


class Trajectories(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, parent=None, width=800, height=600):
        tkinter.Frame.__init__(self, parent)
        ViewBase.__init__(
            self,
            model,
            controller,
            "trajectories",
            parent=parent,
            width=width,
            height=height,
        )

    def _setupView(self, model, controller, **kwargs):
        self.__parent = kwargs["parent"]
        self.__width = kwargs["width"]
        self.__height = kwargs["height"]

        # self.init_buttons()

        self.__parent.grid_columnconfigure(10)

    def __setup_buttons(self, xtypes, ytypes, yinit, xinit, devices):
        self._var_devices = tkinter.StringVar(self.__parent)
        # devices = [str(dev) for dev in range(1, 100)]
        self._var_devices.set(devices[0])

        self._variablex = tkinter.StringVar(self.__parent)
        self._variablex.set(yinit)  # default value

        self._variabley = tkinter.StringVar(self.__parent)
        self._variabley.set(xinit)  # default value

        # self._controller_update_plot = self._controller.get_callback(
        #     "iv_plot",
        #     id=self._name + "_plot",
        #     xvar=self._variablex,
        #     yvar=self._variabley,
        #     devices=self._var_devices,
        # )

        self._controller_update_plot = self._controller.get_callback(
            "iv_plot",
            id=self._name + "_plot",
            xvar=self._variablex,
            yvar=self._variabley,
            devices=self._var_devices,
        )

        self._device_menu = tkinter.OptionMenu(
            self.__parent,
            self._var_devices,
            *devices,
            command=self._controller_update_plot
        )

        # self._device_label = tkinter.Label(self.__parent, text="Device", width=20)
        self._x_label = tkinter.Label(self.__parent, text="x", width=2)
        self._y_label = tkinter.Label(self.__parent, text="y", width=2)

        self._x_menu = tkinter.OptionMenu(
            self.__parent,
            self._variablex,
            *xtypes,
            command=self._controller_update_plot
        )
        self._y_menu = tkinter.OptionMenu(
            self.__parent,
            self._variabley,
            *ytypes,
            command=self._controller_update_plot
        )

        self.init_plot(self.__parent)

        # self.__parent.columnconfigure(1, weight=1)
        # self.__parent.rowconfigure(1, weight=1)

        top = self.__parent.winfo_toplevel()
        # top.rowconfigure(0, weight=1)
        top.columnconfigure(1, weight=1)
        # self.rowconfigure(0, weight=1)
        self.__parent.columnconfigure(1, weight=1)

    def init_plot(self, master, pady=5):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        self.plot_1 = self.ax.plot([], [], label="1")

        self.ax.grid()

        self.ax.set_xlabel("xlabel")
        self.ax.set_ylabel("ylabel")
        # self.fig.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)

        self._toolbar_frame = tkinter.Frame(master)
        matplotlib.backends.backend_tkagg.NavigationToolbar2Tk(
            self.canvas, self._toolbar_frame
        )

        # self._device_label.grid(row=0, column=0, sticky="nw")
        self._device_menu.grid(row=0, column=0, sticky="nw", pady=pady)
        self._y_label.grid(row=0, column=1, sticky="e", pady=pady)
        self._y_menu.grid(row=0, column=2, sticky="w", pady=pady)
        self._x_label.grid(row=0, column=3, sticky="w", pady=pady)
        self._x_menu.grid(row=0, column=4, sticky="w", pady=pady)

        self.canvas.get_tk_widget().config(width=self.__width, height=self.__height)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=5, sticky="news")
        self._toolbar_frame.grid(row=10, column=0, sticky="sew")

        # self.__plot_button.configure(
        #     command=self._controller_update_plot
        # )

    def update_plot(self, x, y, label, xlabel, ylabel):

        self.ax.clear()
        self.ax.set_ylim(min(y) * 0.9, max(y) * 1.1)
        self.ax.set_xlim(min(x) * 0.9, max(x) * 1.1)
        self.ax.plot(x, y, marker="^", label=label)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.legend()
        self.ax.grid()
        self.canvas.draw()

    def setup_controller(self):
        pass

    def update(self):
        state = self._model.getState()

        # if "max_foms" in list(state.keys()):

        if "time_series" in list(state.keys()):
            xtypes = state["time_series"]["xtypes"]
            ytypes = state["time_series"]["ytypes"]

            xinit = state["time_series"]["xinit"]
            yinit = state["time_series"]["yinit"]

            devices = state["time_series"]["devices"]

            self.__setup_buttons(xtypes, ytypes, xinit, yinit, devices)

            data = state["time_series"]["init_data"]
            self.update_plot(
                data["x"], data["y"], data["label"], data["xlabel"], data["ylabel"]
            )

        elif self._name + "_plot" in list(state.keys()):
            data = state[self._name + "_plot"]

            # print("x {}\ny {}".format(data["x"], data["y"]))

            self.update_plot(
                data["x"], data["y"], data["label"], data["xlabel"], data["ylabel"]
            )
