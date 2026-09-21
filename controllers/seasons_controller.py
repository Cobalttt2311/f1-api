from fastapi import APIRouter, Depends, Path
from services.seasons_service import SeasonsService
from models.seasons import (
    SeasonItem, SeasonCircuitItem, SeasonDriverItem, 
    SeasonConstructorItem, SeasonLineupItem, SeasonWinnerItem, SeasonPoleSitterItem
)
from utils.responses.base_response import BaseResponse
from typing import List

router = APIRouter(prefix="/seasons", tags=["Seasons & Season-Based Participation"])

def get_service() -> SeasonsService:
    return SeasonsService()

@router.get("", response_model=BaseResponse[List[SeasonItem]])
def list_seasons(service: SeasonsService = Depends(get_service)):
    """1.1 List all recorded F1 seasons."""
    return service.get_all_seasons()

@router.get("/{year}/circuits", response_model=BaseResponse[List[SeasonCircuitItem]])
def list_season_circuits(year: int = Path(..., examples=[2023]), service: SeasonsService = Depends(get_service)):
    """2.1 List all circuits used in a specific season."""
    return service.get_season_circuits(year)

@router.get("/{year}/drivers", response_model=BaseResponse[List[SeasonDriverItem]])
def list_season_drivers(year: int = Path(..., examples=[2023]), service: SeasonsService = Depends(get_service)):
    """2.2 List all drivers participating in a specific season."""
    return service.get_season_drivers(year)

@router.get("/{year}/constructors", response_model=BaseResponse[List[SeasonConstructorItem]])
def list_season_constructors(year: int = Path(..., examples=[2023]), service: SeasonsService = Depends(get_service)):
    """2.3 List all constructors competing in a specific season."""
    return service.get_season_constructors(year)

@router.get("/{year}/lineups", response_model=BaseResponse[List[SeasonLineupItem]])
def list_season_lineups(year: int = Path(..., examples=[2023]), service: SeasonsService = Depends(get_service)):
    """2.4 List complete driver lineup per team in a specific season."""
    return service.get_season_lineups(year)

@router.get("/{year}/winners", response_model=BaseResponse[List[SeasonWinnerItem]])
def list_season_winners(year: int = Path(..., examples=[2023]), service: SeasonsService = Depends(get_service)):
    """3.5 List all Grand Prix race winners for a specific season."""
    return service.get_season_winners(year)

@router.get("/{year}/pole-sitters", response_model=BaseResponse[List[SeasonPoleSitterItem]])
def list_season_pole_sitters(year: int = Path(..., examples=[2023]), service: SeasonsService = Depends(get_service)):
    """3.10 List all pole position winners (Qualifying P1) for a specific season."""
    return service.get_season_pole_sitters(year)
