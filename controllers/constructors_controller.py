from fastapi import APIRouter, Depends
from services.constructors_service import ConstructorsService
from models.constructors import ConstructorItem
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/constructors", tags=["Constructors"])

def get_service() -> ConstructorsService:
    return ConstructorsService()

@router.get("", response_model=BaseResponse[List[ConstructorItem]])
def list_constructors(service: ConstructorsService = Depends(get_service)):
    """1.4 List all constructor teams in F1 history."""
    return service.get_all_constructors()
