import io
import pkgutil
import tkinter
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

from reliavision import common
from reliavision.customViewer import LayoutViewer
from reliavision.gui.controllers.interface import ControllerInterface
from reliavision.gui.model.interface import ModelInterface
from reliavision.gui.views.common import ViewBase
from reliavision.gui.views.menubar import MenuBar
from reliavision.gui.views.plot import Plot
from reliavision.gui.views.schematic2 import Schematic
from reliavision.gui.views.trajectories import Trajectories


class MainApplication(ViewBase, tkinter.Frame):
    def __init__(
        self,
        model: ModelInterface,
        controller: ControllerInterface,
        use_quit_dialog=True,
        width=900,
        height=800,
        width_offset_lw=25,
        heigth_offset_lw=100,
        extra_height_for_logo=100,
    ) -> None:
        tkinter.Frame.__init__(self)
        ViewBase.__init__(
            self,
            model,
            controller,
            "main",
            use_quit_dialog=use_quit_dialog,
            width=width,
            height=height,
            width_offset_lw=width_offset_lw,
            heigth_offset_lw=heigth_offset_lw,
            extra_height_for_logo=extra_height_for_logo,
        )

    def _setupView(self, model, controller, **kwargs):
        self._width = kwargs["width"]
        self._height = kwargs["height"]

        self.__width_offset_lw = kwargs["width_offset_lw"]
        self.__heigth_offset_lw = kwargs["heigth_offset_lw"]

        self._window = self.winfo_toplevel()
        self._window.title("ReliaVision")

        self._window.columnconfigure(2, weight=1)
        self._window.rowconfigure(2, weight=1)
        self.setup_tabs()

        self._layout_viewer = None
        self._window.resizable(False, False)
        # self._window.resizable(True, True)

        self._window.geometry(
            "{}x{}".format(self._width, self._height + kwargs["extra_height_for_logo"])
        )

        self.create_logo()

    def create_logo(
        self,
        filepath="../static/logo.png",
        height=50,
        row=1,
        column=0,
        pady=5,
        padx=5,
    ):

        img = Image.open(io.BytesIO(pkgutil.get_data(__name__, filepath)))

        scale = img.width / img.height

        # Resize the Image using resize method
        resized_image = img.resize(
            (int(scale * height), int(height)), Image.Resampling.LANCZOS
        )
        self.logo_img = ImageTk.PhotoImage(resized_image)

        # self.my_img.subsample(50, int(scale * width))

        self.logo_label = tkinter.Label(self._window, image=self.logo_img)
        self.logo_label.grid(row=row, column=column, sticky="e", pady=pady, padx=padx)

    def __on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self._window.destroy()

    def setup_controller(self):
        self._controller.add_view(MenuBar, self)
        self._controller.add_view(Plot, self._tabs["bar_chart"])
        self._controller.add_view(Trajectories, self._tabs["trajectories"])
        self._controller.add_view(Schematic, self._tabs["schematic"])

    def update(self):
        state = self._model.getState()

        if "layoutviewer" in list(state.keys()):
            if not common.layout_empty(state["layoutviewer"]):
                if self._layout_viewer is not None:
                    self._layout_viewer.destroy()

                self._layout_viewer = LayoutViewer(
                    self._tabs["layout"],
                    cells=state["layoutviewer"]["cells"],
                    color=state["layoutviewer"]["colors"],
                    hidden_types=state["layoutviewer"]["hidden_types"],
                    pattern=state["layoutviewer"]["patterns"],
                    width=self._width - self.__width_offset_lw,
                    height=self._height - self.__heigth_offset_lw,
                )

    def setup_tabs(self):

        self._notebook = tkinter.ttk.Notebook(
            self._window, width=self._width, height=self._height
        )

        self._tabs = {}

        for tab_id, title in [
            ("schematic", "Schematic"),
            # ("layout", "Layout"),
            ("bar_chart", "Bar Chart"),
            ("trajectories", "I-V Trajectories"),
        ]:

            self._tabs[tab_id] = tkinter.Frame(self._notebook)
            self._notebook.add(self._tabs[tab_id], text=title)

        self._notebook.grid(row=0, column=0, sticky="new")
