from fastapi import APIRouter, Depends, Query
from services.standings_service import StandingsService
from models.standings import DriverStandingItem, ConstructorStandingItem
from utils.responses.base_response import BaseResponse
from typing import List, Optional

router = APIRouter(prefix="/standings", tags=["Championship Standings"])

def get_service() -> StandingsService:
    return StandingsService()

@router.get("/drivers/latest", response_model=BaseResponse[List[DriverStandingItem]])
def get_latest_driver_standings(service: StandingsService = Depends(get_service)):
    """3.6 Dynamic Latest Driver Standings (as of most recent race in DB)."""
    return service.get_latest_driver_standings()

@router.get("/constructors/latest", response_model=BaseResponse[List[ConstructorStandingItem]])
def get_latest_constructor_standings(service: StandingsService = Depends(get_service)):
    """3.7 Dynamic Latest Constructor Standings (as of most recent race in DB)."""
    return service.get_latest_constructor_standings()

@router.get("/drivers", response_model=BaseResponse[List[DriverStandingItem]])
def get_season_driver_standings(year: int = Query(..., examples=[2023]), service: StandingsService = Depends(get_service)):
    """3.8 Driver championship final/season standings per specific year."""
    return service.get_season_driver_standings(year)

@router.get("/constructors", response_model=BaseResponse[List[ConstructorStandingItem]])
def get_season_constructor_standings(year: int = Query(..., examples=[2023]), service: StandingsService = Depends(get_service)):
    """3.9 Constructor championship final/season standings per specific year."""
    return service.get_season_constructor_standings(year)
