from abc import ABC, abstractmethod


class ViewInterface(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def setup_controller(self):
        """
        Abstract method for callback registration w.r.t. concrete controller
        :return:
        """
        pass
