from abc import ABC, abstractmethod


class ViewInterface(ABC):

    @abstractmethod
    def update(self):
        pass
