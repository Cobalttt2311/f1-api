from fastapi import APIRouter, Depends, Query
from repositories.standings_repository import StandingsRepository
from repositories.interfaces.Istandings_repository import IStandingsRepository
from services.standings_service import StandingsService
from services.interfaces.Istandings_service import IStandingsService
from models.standings import DriverStandingItem, ConstructorStandingItem
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List, Optional

router = APIRouter(prefix="/standings", tags=["Championship Standings"])

def get_repository() -> IStandingsRepository:
    return StandingsRepository()

def get_service(repo: IStandingsRepository = Depends(get_repository)) -> IStandingsService:
    return StandingsService(repo=repo)

@router.get("/drivers/latest", response_model=BaseResponse[List[DriverStandingItem]])
def get_latest_driver_standings(service: IStandingsService = Depends(get_service)):
    """3.6 Dynamic Latest Driver Standings (as of most recent race in DB)."""
    data = service.get_latest_driver_standings()
    return BaseResponse.ok(data=data, message=SuccessMessage.LATEST_DRIVER_STANDINGS_RETRIEVED)

@router.get("/constructors/latest", response_model=BaseResponse[List[ConstructorStandingItem]])
def get_latest_constructor_standings(service: IStandingsService = Depends(get_service)):
    """3.7 Dynamic Latest Constructor Standings (as of most recent race in DB)."""
    data = service.get_latest_constructor_standings()
    return BaseResponse.ok(data=data, message=SuccessMessage.LATEST_CONSTRUCTOR_STANDINGS_RETRIEVED)

@router.get("/drivers", response_model=BaseResponse[List[DriverStandingItem]])
def get_season_driver_standings(year: int = Query(..., examples=[2023]), service: IStandingsService = Depends(get_service)):
    """3.8 Driver championship final/season standings per specific year."""
    data = service.get_season_driver_standings(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_DRIVER_STANDINGS_RETRIEVED)

@router.get("/constructors", response_model=BaseResponse[List[ConstructorStandingItem]])
def get_season_constructor_standings(year: int = Query(..., examples=[2023]), service: IStandingsService = Depends(get_service)):
    """3.9 Constructor championship final/season standings per specific year."""
    data = service.get_season_constructor_standings(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_CONSTRUCTOR_STANDINGS_RETRIEVED)
