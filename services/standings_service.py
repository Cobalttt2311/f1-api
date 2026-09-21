from repositories.standings_repository import StandingsRepository
from models.standings import DriverStandingItem, ConstructorStandingItem
from utils.messages.error_message import ErrorMessage
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from fastapi import HTTPException
from typing import List

class StandingsService:
    def __init__(self):
        self.repo = StandingsRepository()

    def get_latest_driver_standings(self) -> BaseResponse[List[DriverStandingItem]]:
        rows = self.repo.get_latest_driver_standings()
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.DRIVER_STANDINGS_NOT_FOUND)
        data = [DriverStandingItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.LATEST_DRIVER_STANDINGS_RETRIEVED)

    def get_latest_constructor_standings(self) -> BaseResponse[List[ConstructorStandingItem]]:
        rows = self.repo.get_latest_constructor_standings()
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.CONSTRUCTOR_STANDINGS_NOT_FOUND)
        data = [ConstructorStandingItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.LATEST_CONSTRUCTOR_STANDINGS_RETRIEVED)

    def get_season_driver_standings(self, year: int) -> BaseResponse[List[DriverStandingItem]]:
        rows = self.repo.get_season_driver_standings(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.DRIVER_STANDINGS_NOT_FOUND)
        data = [DriverStandingItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_DRIVER_STANDINGS_RETRIEVED)

    def get_season_constructor_standings(self, year: int) -> BaseResponse[List[ConstructorStandingItem]]:
        rows = self.repo.get_season_constructor_standings(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.CONSTRUCTOR_STANDINGS_NOT_FOUND)
        data = [ConstructorStandingItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_CONSTRUCTOR_STANDINGS_RETRIEVED)
