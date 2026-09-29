from repositories.interfaces.Icircuits_repository import ICircuitsRepository
from repositories.circuits_repository import CircuitsRepository
from services.interfaces.Icircuits_service import ICircuitsService
from models.circuits import CircuitItem, CircuitHistoryWinner
from utils.messages.error_message import ErrorMessage
from fastapi import HTTPException
from typing import List, Optional

class CircuitsService(ICircuitsService):
    def __init__(self, repo: Optional[ICircuitsRepository] = None):
        self.repo = repo or CircuitsRepository()

    def get_all_circuits(self) -> List[CircuitItem]:
        rows = self.repo.get_all_circuits()
        return [CircuitItem(**r) for r in rows]

    def get_circuit_history(self, circuit_id: int) -> List[CircuitHistoryWinner]:
        rows = self.repo.get_circuit_history(circuit_id)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.CIRCUIT_HISTORY_NOT_FOUND)
        return [CircuitHistoryWinner(**r) for r in rows]
