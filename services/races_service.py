from repositories.races_repository import RacesRepository
from models.races import (
    RaceCalendarItem, PracticeScheduleItem, SprintScheduleItem,
    RaceResultItem, QualifyingResultItem, SprintResultItem,
    PitStopItem, StartingGridDriver, LapChartItem
)
from utils.messages.error_message import ErrorMessage
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from helpers.date_helper import DateHelper
from fastapi import HTTPException
from typing import List

class RacesService:
    def __init__(self):
        self.repo = RacesRepository()

    def get_race_calendar(self, year: int) -> BaseResponse[List[RaceCalendarItem]]:
        rows = self.repo.get_race_calendar(year)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.RACE_NOT_FOUND)
        
        # Enrich raw UTC times with localized WIB times using DateHelper
        data = [RaceCalendarItem(**DateHelper.enrich_race_calendar_item(r)) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.CALENDAR_RETRIEVED)

    def get_practice_schedule(self, year: int, round_no: int) -> BaseResponse[PracticeScheduleItem]:
        row = self.repo.get_practice_schedule(year, round_no)
        if not row:
            raise HTTPException(status_code=404, detail=ErrorMessage.RACE_NOT_FOUND)
        
        # Enrich raw UTC practice times with localized WIB times using DateHelper
        data = PracticeScheduleItem(**DateHelper.enrich_practice_schedule_item(row))
        return BaseResponse.ok(data=data, message=SuccessMessage.PRACTICE_SCHEDULE_RETRIEVED)

    def get_sprint_schedule(self, year: int) -> BaseResponse[List[SprintScheduleItem]]:
        rows = self.repo.get_sprint_schedule(year)
        if not rows:
            raise HTTPException(status_code=404, detail=f"No sprint races found for season {year}.")
        
        # Enrich raw UTC sprint times with localized WIB times using DateHelper
        data = [SprintScheduleItem(**DateHelper.enrich_sprint_schedule_item(r)) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SPRINT_SCHEDULE_RETRIEVED)

    def get_race_results(self, year: int, round_no: int) -> BaseResponse[List[RaceResultItem]]:
        rows = self.repo.get_race_results(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.RACE_NOT_FOUND)
        data = [RaceResultItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.RACE_RESULTS_RETRIEVED)

    def get_qualifying_results(self, year: int, round_no: int) -> BaseResponse[List[QualifyingResultItem]]:
        rows = self.repo.get_qualifying_results(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.QUALIFYING_RESULTS_NOT_FOUND)
        data = [QualifyingResultItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.QUALIFYING_RESULTS_RETRIEVED)

    def get_sprint_results(self, year: int, round_no: int) -> BaseResponse[List[SprintResultItem]]:
        rows = self.repo.get_sprint_results(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.SPRINT_RESULTS_NOT_FOUND)
        data = [SprintResultItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.SPRINT_RESULTS_RETRIEVED)

    def get_pit_stops(self, year: int, round_no: int) -> BaseResponse[List[PitStopItem]]:
        rows = self.repo.get_pit_stops(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.PIT_STOPS_NOT_FOUND)
        data = [PitStopItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.PIT_STOPS_RETRIEVED)

    def get_starting_grid(self, year: int, race_id: int) -> BaseResponse[List[StartingGridDriver]]:
        rows = self.repo.get_starting_grid(year, race_id)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.STARTING_GRID_NOT_FOUND)
        data = [StartingGridDriver(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.STARTING_GRID_RETRIEVED)

    def get_lap_chart(self, year: int, round_no: int) -> BaseResponse[List[LapChartItem]]:
        rows = self.repo.get_lap_chart(year, round_no)
        if not rows:
            raise HTTPException(status_code=404, detail=ErrorMessage.LAP_CHART_NOT_FOUND)
        data = [LapChartItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.LAP_CHART_RETRIEVED)
