from fastapi import APIRouter, Depends
from repositories.constructors_repository import ConstructorsRepository
from repositories.interfaces.Iconstructors_repository import IConstructorsRepository
from services.constructors_service import ConstructorsService
from services.interfaces.Iconstructors_service import IConstructorsService
from models.constructors import ConstructorItem
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/constructors", tags=["Constructors"])

def get_repository() -> IConstructorsRepository:
    return ConstructorsRepository()

def get_service(repo: IConstructorsRepository = Depends(get_repository)) -> IConstructorsService:
    return ConstructorsService(repo=repo)

@router.get("", response_model=BaseResponse[List[ConstructorItem]])
def list_constructors(service: IConstructorsService = Depends(get_service)):
    """1.4 List all constructor teams in F1 history."""
    data = service.get_all_constructors()
    return BaseResponse.ok(data=data, message=SuccessMessage.CONSTRUCTORS_RETRIEVED)
