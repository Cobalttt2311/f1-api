from fastapi import APIRouter, Depends, Path
from repositories.drivers_repository import DriversRepository
from repositories.interfaces.Idrivers_repository import IDriversRepository
from services.drivers_service import DriversService
from services.interfaces.Idrivers_service import IDriversService
from models.drivers import DriverItem, DriverProfile
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/drivers", tags=["Drivers"])

def get_repository() -> IDriversRepository:
    return DriversRepository()

def get_service(repo: IDriversRepository = Depends(get_repository)) -> IDriversService:
    return DriversService(repo=repo)

@router.get("", response_model=BaseResponse[List[DriverItem]])
def list_drivers(service: IDriversService = Depends(get_service)):
    """1.3 List all drivers in F1 history."""
    data = service.get_all_drivers()
    return BaseResponse.ok(data=data, message=SuccessMessage.DRIVERS_RETRIEVED)

@router.get("/{driver_id}/profile", response_model=BaseResponse[DriverProfile])
def get_driver_profile(driver_id: int = Path(..., examples=[1]), service: IDriversService = Depends(get_service)):
    """1.6 Driver career profile card summary."""
    data = service.get_driver_profile(driver_id)
    return BaseResponse.ok(data=data, message=SuccessMessage.DRIVER_PROFILE_RETRIEVED)
