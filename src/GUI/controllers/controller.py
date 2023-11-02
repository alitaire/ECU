import functools
import os
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
from typing import Any, Callable, Iterable, List, Tuple

from reliavision.gui.controllers.interface import ControllerInterface
from reliavision.gui.model.tkModel import tkModel
from reliavision.gui.views.interface import ViewInterface


class Controller(ControllerInterface):
    def __init__(self, model: tkModel) -> None:
        """
        Controller for tkModel
        :param model: tkModel to access reliavision logic
        """
        super().__init__()

        self.__model = model

    def get_callback(self, funct_id: str, **kwargs: Any) -> Callable:
        """
        get_callback function is used to partially set up call back functions in views. A callback is set by an ID and
        optionally with keyword arguments. The return value is a callable function which can be linked to a callback to
        a tkinter object.
        :param funct_id: Function ID which is linked to function to call
        :param kwargs: optional arguments required for the function call
        :return:partially initialised and callable function
        """
        if funct_id == "update_schematic":
            return functools.partial(
                self.update_schematic, schematic_name=kwargs["schematic_name"]
            )

        elif funct_id == "open_file":
            return functools.partial(
                self.open, filetypes=kwargs["filetypes"], name=kwargs["name"]
            )

        # for buttons
        elif funct_id == "quit_window":
            return functools.partial(self.quit_window, view=kwargs["view"])

        # when window is closed by clicking "x" button
        elif funct_id == "quit_window_x":
            return functools.partial(
                self.quit_window_x,
                view=kwargs["view"],
                use_quit_dialog=kwargs["use_quit_dialog"],
            )

        elif funct_id == "update_plot":
            # print(kwargs)
            return functools.partial(
                self.update_plot,
                name=kwargs["name"],
            )

        elif funct_id == "get_device_aging":
            return functools.partial(
                self.get_device_aging, id=kwargs["id"], fom=kwargs["fom"]
            )

        elif funct_id == "iv_plot":
            # print(kwargs)
            return functools.partial(
                self.iv_plot,
                id=kwargs["id"],
                xvar=kwargs["xvar"],
                yvar=kwargs["yvar"],
                devices=kwargs["devices"],
            )

        elif funct_id == "save_config":
            return functools.partial(
                self.save_config,
                entries=kwargs["entries"],
                view=kwargs["view"],
            )

        elif funct_id == "run_spectre":
            return functools.partial(self.run_spectre)

        raise ValueError("No function for function_id {}".format(funct_id))

    def run_spectre(self) -> None:
        """
        Initialised ageing simulation and assignment.
        """
        self.__model.run_spectre()

    def save_config(self, entries, view):
        """
        Setup callback function to save a config file
        :param entries:
        :param view:
        """
        initialdir = os.getenv("VIRTUOSO_PATH")

        file = asksaveasfile(mode="w", filetypes=[("config files", ".ini")], defaultextension=".ini", initialfile="config", initialdir=initialdir)

        self.__model.generate_config_file(view, entries, file)
        print(f"Config file saved as {file.name}")

        self.__model.init_from_config_file(file.name, "menubar_config")

        self.quit_window(view)

    def update_schematic(self, *args: Any, schematic_name: tkinter.StringVar) -> None:
        """
        Setup callback function for schematic image updates

        :param args: Optional arguments
        :param schematic_name: Image choice variable from view
        """
        self.__model.update_schematic(schematic_name.get())

    def update_schematic2(self, schematic_name) -> None:
        """
        Setup callback function for schematic image updates

        :param schematic_name: Image choice variable from view
        """
        self.__model.update_schematic(schematic_name)

    def iv_plot(
        self,
        *args: Any,
        id: str,
        xvar: tkinter.StringVar,
        yvar: tkinter.StringVar,
        devices: tkinter.StringVar,
    ) -> None:
        """
        Setup callback function to update i-v Curves
        :param args: optional function arguments
        :param id: ID of window
        :param xvar: Choice of terminal current/voltage for x-Axis
        :param yvar: Choice of terminal current/voltage for y-Axis
        :param devices: Chosen device
        :return:
        """
        print("clicked")
        self.__model.iv_plot(id, devices.get(), xvar.get(), yvar.get())

    def get_device_aging(
        self, *args: Any, fom: tkinter.StringVar, id: str = ""
    ) -> None:
        """
        Setup callback function to update ageing plots
        :param args: optional function arguments
        :param fom_name: name of requested FOM
        :param name: ID of tkinter Object. This name is used to assign ageing data to a valid model state
        :return:
        """
        self.__model.get_device_aging(fom.get(), id)

    def update_plot(self, *args, name=""):
        """
        TODO TEST FUNCTION
        :param args:
        :param name:
        :return:
        """
        self.__model.update_plot(name)

    def add_view(self, Window, frame, **kwargs):
        """
        Setup callback function to add a view to views in the model class
        :param Window: View which is added
        :param frame: The tkinter.Frame of the view
        :param kwargs: optional arguments which may be required to setup the view
        :return: initialised view
        """
        assert issubclass(Window, ViewInterface)
        view = Window(self.__model, self, frame, **kwargs)
        self.__model.attach(view)

        return view

    def open(self, filetypes: Iterable[Tuple[str, str]], name: str) -> None:
        """Open a configfile for editing.
        :param filetypes: List of tuples containing info of filetype name and extension, e.g. ("Config Files", "*.ini")
        :param name: ID of config window
        """

        initialdir = os.getenv("VIRTUOSO_PATH")

        self.__filepath = askopenfilename(filetypes=filetypes, initialdir=initialdir)

        self.__model.init_from_config_file(self.__filepath, name)

    def quit_window(self, view):
        """
        Closes a window
        :param view: window to close
        """
        view.master.destroy()
        self.__model.detach(view)
        print("destroyed")

    def quit_window_x(self, view, use_quit_dialog):
        """
        Quits a window with dialog
        :param view: Window to close
        :param use_quit_dialog: option to show a dialog
        :return:
        """
        quit = True

        if use_quit_dialog:
            quit = False
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                quit = True

        if quit:
            view.winfo_toplevel().destroy()
            self.__model.detach(view)
            print("destroyed")
