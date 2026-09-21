from fastapi import APIRouter, Depends, Path
from services.circuits_service import CircuitsService
from models.circuits import CircuitItem, CircuitHistoryWinner
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/circuits", tags=["Circuits"])

def get_service() -> CircuitsService:
    return CircuitsService()

@router.get("", response_model=BaseResponse[List[CircuitItem]])
def list_circuits(service: CircuitsService = Depends(get_service)):
    """1.2 List all F1 circuits worldwide."""
    return service.get_all_circuits()

@router.get("/{circuit_id}/history", response_model=BaseResponse[List[CircuitHistoryWinner]])
def get_circuit_history(circuit_id: int = Path(..., examples=[6]), service: CircuitsService = Depends(get_service)):
    """1.7 Circuit history and past race winners."""
    return service.get_circuit_history(circuit_id)
