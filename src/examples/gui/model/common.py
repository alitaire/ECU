from typing import Any, Dict, List

from reliavision.gui.model.interface import ModelInterface
from reliavision.gui.views.interface import ViewInterface


class ModelBaseClass(ModelInterface):
    _state: Dict[str, Any]
    __views: List[ViewInterface]

    def __init__(self) -> None:
        """
        Defines empty view list and empty state dictionary
        """
        self.__views = []
        self._state = {}

    def attach(self, view: ViewInterface) -> None:

        self.__views.append(view)

    def detach(self, view: ViewInterface) -> None:
        self.__views.remove(view)

    def notify(self) -> None:
        for view in self.__views:
            view.update()

    def getNumberOfViews(self) -> int:
        """
        Return length of views list
        :return:
        """
        return len(self.__views)

    def getState(self) -> dict:
        return self._state

    # def getFilteredState(self, name: str) -> dict:
    #     pass
