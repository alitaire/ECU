from abc import ABC, abstractmethod

from reliavision.gui.views.interface import ViewInterface


class ModelInterface(ABC):
    @abstractmethod
    def attach(self, view) -> None:
        """
        Add a window to the view list
        :param view: Window of the GUI
        """
        pass

    @abstractmethod
    def detach(self, view: ViewInterface) -> None:
        """
        Removes a window from the view list
        :param view: Window to remove
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        sends update signal to registered views
        :return:
        """
        pass

    @abstractmethod
    def getState(self) -> dict:
        """
        This function is not part of the Observer model but is very handy exchanging data with view objects only on the interface level
        :return:
        """
        pass

    # @abstractmethod
    # def getFilteredState(self, name: str) -> dict:
    #     pass
