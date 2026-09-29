from repositories.interfaces.Idrivers_repository import IDriversRepository
from repositories.drivers_repository import DriversRepository
from services.interfaces.Idrivers_service import IDriversService
from models.drivers import DriverItem, DriverProfile
from utils.messages.error_message import ErrorMessage
from fastapi import HTTPException
from typing import List, Optional

class DriversService(IDriversService):
    def __init__(self, repo: Optional[IDriversRepository] = None):
        self.repo = repo or DriversRepository()

    def get_all_drivers(self) -> List[DriverItem]:
        rows = self.repo.get_all_drivers()
        return [DriverItem(**r) for r in rows]

    def get_driver_profile(self, driver_id: int) -> DriverProfile:
        row = self.repo.get_driver_profile(driver_id)
        if not row:
            raise HTTPException(status_code=404, detail=ErrorMessage.DRIVER_NOT_FOUND)
        return DriverProfile(**row)
