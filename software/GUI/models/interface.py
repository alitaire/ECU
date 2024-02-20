from abc import ABC, abstractmethod


class ModelInterface(ABC):
    def __init__(self):
        self._observers = []
        self.__state = {}

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def getState(self):
        return  self.__state

    def setState(self, state, value):
        self.__state[state] = value

    def delState(self, state):
        self.__state.pop(state)
