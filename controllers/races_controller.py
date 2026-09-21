from fastapi import APIRouter, Depends, Path, Query
from services.races_service import RacesService
from models.races import (
    RaceCalendarItem, PracticeScheduleItem, SprintScheduleItem,
    RaceResultItem, QualifyingResultItem, SprintResultItem,
    PitStopItem, StartingGridDriver, LapChartItem
)
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/races", tags=["Races & Race Weekend"])

def get_service() -> RacesService:
    return RacesService()

@router.get("/calendar", response_model=BaseResponse[List[RaceCalendarItem]])
def get_calendar(year: int = Query(..., examples=[2023]), service: RacesService = Depends(get_service)):
    """1.5 Race calendar with has_sprint indicator, UTC & WIB race times."""
    return service.get_race_calendar(year)

@router.get("/{year}/{round_no}/practice-schedule", response_model=BaseResponse[PracticeScheduleItem])
def get_practice_schedule(
    year: int = Path(..., examples=[2023]), 
    round_no: int = Path(..., examples=[1]), 
    service: RacesService = Depends(get_service)
):
    """1.8 Dedicated Free Practice Sessions Schedule (FP1, FP2, FP3) in UTC & WIB times."""
    return service.get_practice_schedule(year, round_no)

@router.get("/{year}/sprint-schedule", response_model=BaseResponse[List[SprintScheduleItem]])
def get_sprint_schedule(
    year: int = Path(..., examples=[2023]), 
    service: RacesService = Depends(get_service)
):
    """1.9 Dedicated Sprint Race Weekends Schedule for a Season in UTC & WIB times."""
    return service.get_sprint_schedule(year)

@router.get("/{year}/{round_no}/results", response_model=BaseResponse[List[RaceResultItem]])
def get_race_results(year: int, round_no: int, service: RacesService = Depends(get_service)):
    """3.1 Full Grand Prix race results for a specific round."""
    return service.get_race_results(year, round_no)

@router.get("/{year}/{round_no}/qualifying", response_model=BaseResponse[List[QualifyingResultItem]])
def get_qualifying_results(year: int, round_no: int, service: RacesService = Depends(get_service)):
    """3.2 Qualifying session results (Q1, Q2, Q3)."""
    return service.get_qualifying_results(year, round_no)

@router.get("/{year}/{round_no}/sprint", response_model=BaseResponse[List[SprintResultItem]])
def get_sprint_results(year: int, round_no: int, service: RacesService = Depends(get_service)):
    """3.3 Sprint race results."""
    return service.get_sprint_results(year, round_no)

@router.get("/{year}/{round_no}/pit-stops", response_model=BaseResponse[List[PitStopItem]])
def get_pit_stops(year: int, round_no: int, service: RacesService = Depends(get_service)):
    """3.4 Pit stops history and durations."""
    return service.get_pit_stops(year, round_no)

@router.get("/{year}/{race_id}/starting-grid", response_model=BaseResponse[List[StartingGridDriver]])
def get_starting_grid(year: int, race_id: int, service: RacesService = Depends(get_service)):
    """3.11 Official starting grid incorporating penalties and pit lane starts."""
    return service.get_starting_grid(year, race_id)

@router.get("/{year}/{round_no}/lap-chart", response_model=BaseResponse[List[LapChartItem]])
def get_lap_chart(year: int, round_no: int, service: RacesService = Depends(get_service)):
    """4.10 Lap-by-lap race position progression tracking."""
    return service.get_lap_chart(year, round_no)
