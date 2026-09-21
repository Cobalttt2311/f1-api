from repositories.drivers_repository import DriversRepository
from models.drivers import DriverItem, DriverProfile
from utils.messages.error_message import ErrorMessage
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from fastapi import HTTPException
from typing import List

class DriversService:
    def __init__(self):
        self.repo = DriversRepository()

    def get_all_drivers(self) -> BaseResponse[List[DriverItem]]:
        rows = self.repo.get_all_drivers()
        data = [DriverItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.DRIVERS_RETRIEVED)

    def get_driver_profile(self, driver_id: int) -> BaseResponse[DriverProfile]:
        row = self.repo.get_driver_profile(driver_id)
        if not row:
            raise HTTPException(status_code=404, detail=ErrorMessage.DRIVER_NOT_FOUND)
        data = DriverProfile(**row)
        return BaseResponse.ok(data=data, message=SuccessMessage.DRIVER_PROFILE_RETRIEVED)
