from abc import ABC, abstractmethod
from typing import Any, Callable


class ControllerInterface(ABC):
    @abstractmethod
    def get_callback(self, funct_id: str, **kwargs: Any) -> Callable:
        """
        delegates callback data to model

        :param id: internal identifier which is used to determine operation on model
        :param kwargs: variables from view
        :return:
        """
        pass
