import tkinter

from reliavision.gui.views.common import ViewBase
from reliavision.gui.views.configrunwindow import ConfigRunWindow
from reliavision.gui.views.configwindow import ConfigWindow
from reliavision.gui.views.technologywindow import TechnologyWindow


class MenuBar(ViewBase, tkinter.Frame):
    def __init__(self, model, controller, parent=None):
        tkinter.Frame.__init__(self, parent)
        ViewBase.__init__(self, model, controller, "menubar", parent=parent)

        # self._funct = self._controller.open_window("technology", self.master)

    def _setupView(self, model, controller, **kwargs):
        # self._controller = controller
        self.__parent = kwargs["parent"]
        self.__window = self.__parent._window

        self.__menubar = tkinter.Menu(self.__parent)

        # entries
        self.file()
        # self.export()
        self.run()

        self.__window.config(menu=self.__menubar)

    def setup_controller(self):
        pass

    def update(self):
        self._state = self._model.getState()
        # print(self._name)
        # print(self._state)
        # print("---")

    def file(self):
        filemenu = tkinter.Menu(self.__window, tearoff=False)
        filemenu.add_command(
            label="New",
            command=lambda: self._controller.add_view(
                ConfigWindow, tkinter.Toplevel(self.master), width=30
            ),
        )
        filemenu.add_command(
            label="Open",
            command=self._controller.get_callback(
                "open_file",
                name=self._name + "_config",
                filetypes=[("Config Files", "*.ini"), ("All Files", "*.*")],
            ),
        )
        filemenu.add_command(
            label="Technology",
            command=lambda: self._controller.add_view(
                TechnologyWindow, tkinter.Toplevel(self.master)
            ),
        )

        self.__menubar.add_cascade(label="File", menu=filemenu)

    def run(self):
        filemenu = tkinter.Menu(self.__window, tearoff=False)
        filemenu.add_command(
            label="Run Simulation",
            command=self._controller.get_callback(
                "run_spectre",
            ),
        )
        filemenu.add_command(
            label="Options",
            command=lambda: self._controller.add_view(
                ConfigRunWindow, tkinter.Toplevel(self.master)
            ),
        )

        self.__menubar.add_cascade(label="Run", menu=filemenu)

    def print_run(self):
        print("running")

    def export(self):
        filemenu = tkinter.Menu(self.__window, tearoff=False)
        filemenu.add_command(label="Schematic")
        filemenu.add_command(label="Netlist")
        filemenu.add_command(label="Configuration")

        self.__menubar.add_cascade(label="Export", menu=filemenu)

    # def _open_file(self):
    #     """Open a file for editing."""
    #
    #     self.__filepath = askopenfilename(
    #         filetypes=[("Config Files", "*.ini"), ("All Files", "*.*")]
    #     )

    # def get_file_path(self):
    #     return self.__filepath

    # def call_run_options(self):
    #     ConfigRunWindow(tkinter.Toplevel(self.master))

    # def call_config_window(self):
    #     ConfigWindow(tkinter.Toplevel(self.master))

    # def call_technology(self):
    #     TechnologyWindow(tkinter.Toplevel(self.master))

    # def call_restore_window(self):
    #     RestoreWindow(tkinter.Toplevel(self.master))
