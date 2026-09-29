from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IConstructorsRepository(ABC):
    @abstractmethod
    def get_all_constructors(self) -> List[Dict[str, Any]]: ...
