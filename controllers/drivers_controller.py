from fastapi import APIRouter, Depends, Path
from services.drivers_service import DriversService
from models.drivers import DriverItem, DriverProfile
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/drivers", tags=["Drivers"])

def get_service() -> DriversService:
    return DriversService()

@router.get("", response_model=BaseResponse[List[DriverItem]])
def list_drivers(service: DriversService = Depends(get_service)):
    """1.3 List all drivers in F1 history."""
    return service.get_all_drivers()

@router.get("/{driver_id}/profile", response_model=BaseResponse[DriverProfile])
def get_driver_profile(driver_id: int = Path(..., examples=[1]), service: DriversService = Depends(get_service)):
    """1.6 Driver profile and career summary statistics."""
    return service.get_driver_profile(driver_id)
