from abc import ABC, abstractmethod
from typing import List
from models.constructors import ConstructorItem

class IConstructorsService(ABC):
    @abstractmethod
    def get_all_constructors(self) -> List[ConstructorItem]: ...
