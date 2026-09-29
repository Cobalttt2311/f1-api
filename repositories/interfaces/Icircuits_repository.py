from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ICircuitsRepository(ABC):
    @abstractmethod
    def get_all_circuits(self) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_circuit_history(self, circuit_id: int) -> List[Dict[str, Any]]: ...
