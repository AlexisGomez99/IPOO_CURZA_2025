from abc import ABC, abstractmethod


class Domesticable(ABC):
    @abstractmethod
    def entrenar(self):
        pass
