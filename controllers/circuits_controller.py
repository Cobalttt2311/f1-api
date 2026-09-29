from fastapi import APIRouter, Depends, Path
from repositories.circuits_repository import CircuitsRepository
from repositories.interfaces.Icircuits_repository import ICircuitsRepository
from services.circuits_service import CircuitsService
from services.interfaces.Icircuits_service import ICircuitsService
from models.circuits import CircuitItem, CircuitHistoryWinner
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/circuits", tags=["Circuits"])

def get_repository() -> ICircuitsRepository:
    return CircuitsRepository()

def get_service(repo: ICircuitsRepository = Depends(get_repository)) -> ICircuitsService:
    return CircuitsService(repo=repo)

@router.get("", response_model=BaseResponse[List[CircuitItem]])
def list_circuits(service: ICircuitsService = Depends(get_service)):
    """1.2 List all F1 circuits worldwide."""
    data = service.get_all_circuits()
    return BaseResponse.ok(data=data, message=SuccessMessage.CIRCUITS_RETRIEVED)

@router.get("/{circuit_id}/history", response_model=BaseResponse[List[CircuitHistoryWinner]])
def get_circuit_history(circuit_id: int = Path(..., examples=[1]), service: ICircuitsService = Depends(get_service)):
    """2.5 List historical race winners at a specific circuit."""
    data = service.get_circuit_history(circuit_id)
    return BaseResponse.ok(data=data, message=SuccessMessage.CIRCUIT_HISTORY_RETRIEVED)
