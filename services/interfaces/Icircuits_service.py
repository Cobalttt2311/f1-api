from abc import ABC, abstractmethod
from typing import List
from models.circuits import CircuitItem, CircuitHistoryWinner

class ICircuitsService(ABC):
    @abstractmethod
    def get_all_circuits(self) -> List[CircuitItem]: ...

    @abstractmethod
    def get_circuit_history(self, circuit_id: int) -> List[CircuitHistoryWinner]: ...
