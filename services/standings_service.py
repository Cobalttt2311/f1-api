from repositories.interfaces.Istandings_repository import IStandingsRepository
from repositories.standings_repository import StandingsRepository
from services.interfaces.Istandings_service import IStandingsService
from models.standings import DriverStandingItem, ConstructorStandingItem
from utils.messages.error_message import ErrorMessage
from fastapi import HTTPException
from typing import List, Optional

class StandingsService(IStandingsService):
    def __init__(self, repo: Optional[IStandingsRepository] = None):
        self.repo = repo or StandingsRepository()

    def get_latest_driver_standings(self) -> List[DriverStandingItem]:
        rows = self.repo.get_latest_driver_standings()
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.DRIVER_STANDINGS_NOT_FOUND)
        return [DriverStandingItem(**r) for r in rows]

    def get_latest_constructor_standings(self) -> List[ConstructorStandingItem]:
        rows = self.repo.get_latest_constructor_standings()
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.CONSTRUCTOR_STANDINGS_NOT_FOUND)
        return [ConstructorStandingItem(**r) for r in rows]

    def get_season_driver_standings(self, year: int) -> List[DriverStandingItem]:
        rows = self.repo.get_season_driver_standings(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.DRIVER_STANDINGS_NOT_FOUND)
        return [DriverStandingItem(**r) for r in rows]

    def get_season_constructor_standings(self, year: int) -> List[ConstructorStandingItem]:
        rows = self.repo.get_season_constructor_standings(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.CONSTRUCTOR_STANDINGS_NOT_FOUND)
        return [ConstructorStandingItem(**r) for r in rows]
