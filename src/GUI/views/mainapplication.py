import math
import sys
from PySide6.QtGui import QPainter, QColor, QLinearGradient, QPen, QPaintEvent
from PySide6.QtCore import QPoint, Qt, QPointF, Slot, QThread, Signal
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1024, 760)

        widget = QWidget()
        hBox = QHBoxLayout()
        self.speedWidget1 = SpeedWidget()
        self.speedWidget1.maxUnit = 100
        self.speedWidget1.unit = "%"
        self.speedWidget2 = SpeedWidget()
        self.speedWidget2.maxUnit = 150
        self.speedWidget2.unit = "°C"

        hBox.addWidget(self.speedWidget1)
        hBox.addWidget(self.speedWidget2)

        hBox2 = QHBoxLayout()

        vBox = QVBoxLayout()
        vBox.addLayout(hBox)
        # vBox.addLayout(hBox2)

        widget.setLayout(vBox)
        self.setCentralWidget(widget)


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

    def setup_controller(self):
        self._controller.add_view(MenuBar, self)
        self._controller.add_view(Plot, self._tabs["bar_chart"])
        self._controller.add_view(Trajectories, self._tabs["trajectories"])
        self._controller.add_view(Schematic, self._tabs["schematic"])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self.speedWidget.increment_speed()
        elif event.key() == Qt.Key_Minus:
            self.speedWidget.decrement_speed()

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
