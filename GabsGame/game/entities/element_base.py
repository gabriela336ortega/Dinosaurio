from pygame import Surface
from abc import ABC, abstractmethod

class BaseElement(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def update(self) -> None:
        """
        Actualiza el estado de una entidad
        """
        pass
    
    @abstractmethod
    def draw(self, surface: Surface) -> Surface:
        """
        Dibuja o renderiza una entidad en la superficie dada
        """
        pass