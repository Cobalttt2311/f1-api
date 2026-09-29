from repositories.interfaces.Iraces_repository import IRacesRepository
from repositories.races_repository import RacesRepository
from services.interfaces.Iraces_service import IRacesService
from models.races import (
    RaceCalendarItem, PracticeScheduleItem, SprintScheduleItem,
    RaceResultItem, QualifyingResultItem, SprintResultItem,
    PitStopItem, StartingGridDriver, LapChartItem
)
from utils.messages.error_message import ErrorMessage
from helpers.date_helper import DateHelper
from fastapi import HTTPException
from typing import List, Optional

class RacesService(IRacesService):
    def __init__(self, repo: Optional[IRacesRepository] = None):
        self.repo = repo or RacesRepository()

    def get_race_calendar(self, year: int) -> List[RaceCalendarItem]:
        rows = self.repo.get_race_calendar(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.RACE_NOT_FOUND)
        return [RaceCalendarItem(**DateHelper.enrich_race_calendar_item(r)) for r in rows]

    def get_practice_schedule(self, year: int, round_no: int) -> PracticeScheduleItem:
        row = self.repo.get_practice_schedule(year, round_no)
        if not row:
            raise HTTPException(status_code=404, detail=ErrorMessage.RACE_NOT_FOUND)
        return PracticeScheduleItem(**DateHelper.enrich_practice_schedule_item(row))

    def get_sprint_schedule(self, year: int) -> List[SprintScheduleItem]:
        rows = self.repo.get_sprint_schedule(year)
        if not rows:
            raise HTTPException(status_code=404, detail=f"No sprint races found for season {year}.")
        return [SprintScheduleItem(**DateHelper.enrich_sprint_schedule_item(r)) for r in rows]

    def get_race_results(self, year: int, round_no: int) -> List[RaceResultItem]:
        rows = self.repo.get_race_results(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.RACE_NOT_FOUND)
        return [RaceResultItem(**r) for r in rows]

    def get_qualifying_results(self, year: int, round_no: int) -> List[QualifyingResultItem]:
        rows = self.repo.get_qualifying_results(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.QUALIFYING_RESULTS_NOT_FOUND)
        return [QualifyingResultItem(**r) for r in rows]

    def get_sprint_results(self, year: int, round_no: int) -> List[SprintResultItem]:
        rows = self.repo.get_sprint_results(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SPRINT_RESULTS_NOT_FOUND)
        return [SprintResultItem(**r) for r in rows]

    def get_pit_stops(self, year: int, round_no: int) -> List[PitStopItem]:
        rows = self.repo.get_pit_stops(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.PIT_STOPS_NOT_FOUND)
        return [PitStopItem(**r) for r in rows]

    def get_starting_grid(self, year: int, race_id: int) -> List[StartingGridDriver]:
        rows = self.repo.get_starting_grid(year, race_id)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.STARTING_GRID_NOT_FOUND)
        return [StartingGridDriver(**r) for r in rows]

    def get_lap_chart(self, year: int, round_no: int) -> List[LapChartItem]:
        rows = self.repo.get_lap_chart(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.LAP_CHART_NOT_FOUND)
        return [LapChartItem(**r) for r in rows]
