from repositories.seasons_repository import SeasonsRepository
from models.seasons import (
    SeasonItem, SeasonCircuitItem, SeasonDriverItem, 
    SeasonConstructorItem, SeasonLineupItem, SeasonWinnerItem, SeasonPoleSitterItem
)
from utils.messages.error_message import ErrorMessage
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from fastapi import HTTPException
from typing import List

class SeasonsService:
    def __init__(self):
        self.repo = SeasonsRepository()

    def get_all_seasons(self) -> BaseResponse[List[SeasonItem]]:
        rows = self.repo.get_all_seasons()
        data = [SeasonItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASONS_RETRIEVED)

    def get_season_circuits(self, year: int) -> BaseResponse[List[SeasonCircuitItem]]:
        rows = self.repo.get_season_circuits(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        data = [SeasonCircuitItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_CIRCUITS_RETRIEVED)

    def get_season_drivers(self, year: int) -> BaseResponse[List[SeasonDriverItem]]:
        rows = self.repo.get_season_drivers(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        data = [SeasonDriverItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_DRIVERS_RETRIEVED)

    def get_season_constructors(self, year: int) -> BaseResponse[List[SeasonConstructorItem]]:
        rows = self.repo.get_season_constructors(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        data = [SeasonConstructorItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_CONSTRUCTORS_RETRIEVED)

    def get_season_lineups(self, year: int) -> BaseResponse[List[SeasonLineupItem]]:
        rows = self.repo.get_season_lineups(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        data = [SeasonLineupItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_LINEUPS_RETRIEVED)

    def get_season_winners(self, year: int) -> BaseResponse[List[SeasonWinnerItem]]:
        rows = self.repo.get_season_winners(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        data = [SeasonWinnerItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_WINNERS_RETRIEVED)

    def get_season_pole_sitters(self, year: int) -> BaseResponse[List[SeasonPoleSitterItem]]:
        rows = self.repo.get_season_pole_sitters(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        data = [SeasonPoleSitterItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_POLE_SITTERS_RETRIEVED)
