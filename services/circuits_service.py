from repositories.circuits_repository import CircuitsRepository
from models.circuits import CircuitItem, CircuitHistoryWinner
from utils.messages.error_message import ErrorMessage
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from fastapi import HTTPException
from typing import List

class CircuitsService:
    def __init__(self):
        self.repo = CircuitsRepository()

    def get_all_circuits(self) -> BaseResponse[List[CircuitItem]]:
        rows = self.repo.get_all_circuits()
        data = [CircuitItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.CIRCUITS_RETRIEVED)

    def get_circuit_history(self, circuit_id: int) -> BaseResponse[List[CircuitHistoryWinner]]:
        rows = self.repo.get_circuit_history(circuit_id)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.CIRCUIT_HISTORY_NOT_FOUND)
        data = [CircuitHistoryWinner(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.CIRCUIT_HISTORY_RETRIEVED)
