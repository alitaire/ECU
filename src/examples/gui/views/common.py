from abc import abstractmethod
from typing import Any, Dict

from reliavision.gui.controllers.interface import ControllerInterface
from reliavision.gui.model.interface import ModelInterface
from reliavision.gui.views.interface import ViewInterface


class ViewBase(ViewInterface):
    _state: Dict[str, Any]

    def __init__(
        self,
        model: ModelInterface,
        controller: ControllerInterface,
        name: str,
        use_quit_dialog=False,
        **kwargs: Any
    ) -> None:
        self._name = name
        self._state = {}
        self._controller = controller
        self._model = model
        self._setupView(model, controller, **kwargs)
        self.setup_controller_base(use_quit_dialog)
        self.setup_controller()
        # self.setup_controller_base(use_quit_dialog)

    def setup_controller_base(self, use_quit_dialog):
        self.winfo_toplevel().protocol(
            "WM_DELETE_WINDOW",
            self._controller.get_callback(
                "quit_window_x", view=self, use_quit_dialog=use_quit_dialog
            ),
        )

    @abstractmethod
    def _setupView(
        self, model: ModelInterface, controller: ControllerInterface, **kwargs
    ):
        """
        Only this has to be implemented in concrete view subclasses
        :param kwargs:
        :return:
        """
        pass
