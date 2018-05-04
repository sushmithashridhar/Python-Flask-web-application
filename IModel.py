from abc import ABC, abstractmethod

class IModel(ABC):

    @abstractmethod
    def fetchall(self, dict):
        pass
