from fastapi import APIRouter, Depends, Path
from repositories.seasons_repository import SeasonsRepository
from repositories.interfaces.Iseasons_repository import ISeasonsRepository
from services.seasons_service import SeasonsService
from services.interfaces.Iseasons_service import ISeasonsService
from models.seasons import (
    SeasonItem, SeasonCircuitItem, SeasonDriverItem, 
    SeasonConstructorItem, SeasonLineupItem, SeasonWinnerItem, SeasonPoleSitterItem
)
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/seasons", tags=["Seasons & Season-Based Participation"])

def get_repository() -> ISeasonsRepository:
    return SeasonsRepository()

def get_service(repo: ISeasonsRepository = Depends(get_repository)) -> ISeasonsService:
    return SeasonsService(repo=repo)

@router.get("", response_model=BaseResponse[List[SeasonItem]])
def list_seasons(service: ISeasonsService = Depends(get_service)):
    """1.1 List all recorded F1 seasons."""
    data = service.get_all_seasons()
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASONS_RETRIEVED)

@router.get("/{year}/circuits", response_model=BaseResponse[List[SeasonCircuitItem]])
def list_season_circuits(year: int = Path(..., examples=[2023]), service: ISeasonsService = Depends(get_service)):
    """2.1 List all circuits used in a specific season."""
    data = service.get_season_circuits(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_CIRCUITS_RETRIEVED)

@router.get("/{year}/drivers", response_model=BaseResponse[List[SeasonDriverItem]])
def list_season_drivers(year: int = Path(..., examples=[2023]), service: ISeasonsService = Depends(get_service)):
    """2.2 List all drivers participating in a specific season."""
    data = service.get_season_drivers(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_DRIVERS_RETRIEVED)

@router.get("/{year}/constructors", response_model=BaseResponse[List[SeasonConstructorItem]])
def list_season_constructors(year: int = Path(..., examples=[2023]), service: ISeasonsService = Depends(get_service)):
    """2.3 List all constructors competing in a specific season."""
    data = service.get_season_constructors(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_CONSTRUCTORS_RETRIEVED)

@router.get("/{year}/lineups", response_model=BaseResponse[List[SeasonLineupItem]])
def list_season_lineups(year: int = Path(..., examples=[2023]), service: ISeasonsService = Depends(get_service)):
    """2.4 List complete driver lineup per team in a specific season."""
    data = service.get_season_lineups(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_LINEUPS_RETRIEVED)

@router.get("/{year}/winners", response_model=BaseResponse[List[SeasonWinnerItem]])
def list_season_winners(year: int = Path(..., examples=[2023]), service: ISeasonsService = Depends(get_service)):
    """3.5 List all Grand Prix race winners for a specific season."""
    data = service.get_season_winners(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_WINNERS_RETRIEVED)

@router.get("/{year}/pole-sitters", response_model=BaseResponse[List[SeasonPoleSitterItem]])
def list_season_pole_sitters(year: int = Path(..., examples=[2023]), service: ISeasonsService = Depends(get_service)):
    """3.10 List all pole position winners (Qualifying P1) for a specific season."""
    data = service.get_season_pole_sitters(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.SEASON_POLE_SITTERS_RETRIEVED)
