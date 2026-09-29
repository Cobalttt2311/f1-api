from repositories.interfaces.Iseasons_repository import ISeasonsRepository
from repositories.seasons_repository import SeasonsRepository
from services.interfaces.Iseasons_service import ISeasonsService
from models.seasons import (
    SeasonItem, SeasonCircuitItem, SeasonDriverItem, 
    SeasonConstructorItem, SeasonLineupItem, SeasonWinnerItem, SeasonPoleSitterItem
)
from utils.messages.error_message import ErrorMessage
from fastapi import HTTPException
from typing import List, Optional

class SeasonsService(ISeasonsService):
    def __init__(self, repo: Optional[ISeasonsRepository] = None):
        self.repo = repo or SeasonsRepository()

    def get_all_seasons(self) -> List[SeasonItem]:
        rows = self.repo.get_all_seasons()
        return [SeasonItem(**r) for r in rows]

    def get_season_circuits(self, year: int) -> List[SeasonCircuitItem]:
        rows = self.repo.get_season_circuits(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        return [SeasonCircuitItem(**r) for r in rows]

    def get_season_drivers(self, year: int) -> List[SeasonDriverItem]:
        rows = self.repo.get_season_drivers(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        return [SeasonDriverItem(**r) for r in rows]

    def get_season_constructors(self, year: int) -> List[SeasonConstructorItem]:
        rows = self.repo.get_season_constructors(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        return [SeasonConstructorItem(**r) for r in rows]

    def get_season_lineups(self, year: int) -> List[SeasonLineupItem]:
        rows = self.repo.get_season_lineups(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        return [SeasonLineupItem(**r) for r in rows]

    def get_season_winners(self, year: int) -> List[SeasonWinnerItem]:
        rows = self.repo.get_season_winners(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        return [SeasonWinnerItem(**r) for r in rows]

    def get_season_pole_sitters(self, year: int) -> List[SeasonPoleSitterItem]:
        rows = self.repo.get_season_pole_sitters(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SEASON_NOT_FOUND)
        return [SeasonPoleSitterItem(**r) for r in rows]
