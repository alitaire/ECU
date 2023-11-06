from abc import ABC, abstractmethod


class ModelInterface(ABC):
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
