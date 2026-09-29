from fastapi import APIRouter, Depends, Query
from repositories.analytics_repository import AnalyticsRepository
from repositories.interfaces.Ianalytics_repository import IAnalyticsRepository
from services.analytics_service import AnalyticsService
from services.interfaces.Ianalytics_service import IAnalyticsService
from models.analytics import (
    BiggestMoverItem, PitStopEfficiencyItem, PoleToWinItem,
    HighDNFCircuitItem, DeepGridWinItem, LapsLedItem,
    FastestSpeedItem, AllTimeWinnerItem, TeammateQualiBattleItem,
    DriverRollingFormItem, CumulativePointsItem, ConstructorOneTwoItem,
    YoungestWinnerItem, CircuitMasterItem,
    LastSyncMetadataItem
)
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List, Optional

router = APIRouter(prefix="/analytics", tags=["Strategy & Performance Analytics"])

def get_repository() -> IAnalyticsRepository:
    return AnalyticsRepository()

def get_service(repo: IAnalyticsRepository = Depends(get_repository)) -> IAnalyticsService:
    return AnalyticsService(repo=repo)

@router.get("/biggest-movers", response_model=BaseResponse[List[BiggestMoverItem]])
def get_biggest_movers(year: int = Query(2023), limit: int = Query(10), service: IAnalyticsService = Depends(get_service)):
    """4.1 Greatest comebacks / positions gained from starting grid."""
    data = service.get_biggest_movers(year, limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.BIGGEST_MOVERS_RETRIEVED)

@router.get("/pit-stop-efficiency", response_model=BaseResponse[List[PitStopEfficiencyItem]])
def get_pit_stop_efficiency(year: int = Query(2023), service: IAnalyticsService = Depends(get_service)):
    """4.2 Pit stop efficiency and average duration by constructor."""
    data = service.get_pit_stop_efficiency(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.PIT_STOP_EFFICIENCY_RETRIEVED)

@router.get("/pole-to-win-rate", response_model=BaseResponse[List[PoleToWinItem]])
def get_pole_to_win_rate(start_year: int = Query(2015), service: IAnalyticsService = Depends(get_service)):
    """4.3 Pole-to-win conversion rate across seasons."""
    data = service.get_pole_to_win_rate(start_year)
    return BaseResponse.ok(data=data, message=SuccessMessage.POLE_TO_WIN_RETRIEVED)

@router.get("/high-dnf-circuits", response_model=BaseResponse[List[HighDNFCircuitItem]])
def get_high_dnf_circuits(limit: int = Query(10), service: IAnalyticsService = Depends(get_service)):
    """4.4 Most incident-prone and high-DNF circuits."""
    data = service.get_high_dnf_circuits(limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.HIGH_DNF_CIRCUITS_RETRIEVED)

@router.get("/deep-grid-wins", response_model=BaseResponse[List[DeepGridWinItem]])
def get_deep_grid_wins(min_grid: int = Query(10), limit: int = Query(10), service: IAnalyticsService = Depends(get_service)):
    """4.5 Historical wins from deepest starting grid positions (P10+)."""
    data = service.get_deep_grid_wins(min_grid, limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.DEEP_GRID_WINS_RETRIEVED)

@router.get("/most-laps-led", response_model=BaseResponse[List[LapsLedItem]])
def get_most_laps_led(limit: int = Query(15), service: IAnalyticsService = Depends(get_service)):
    """4.6 Drivers with most laps led in P1 across history."""
    data = service.get_most_laps_led(limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.MOST_LAPS_LED_RETRIEVED)

@router.get("/fastest-speeds", response_model=BaseResponse[List[FastestSpeedItem]])
def get_fastest_speeds(limit: int = Query(10), service: IAnalyticsService = Depends(get_service)):
    """4.7 Fastest race speed recorded in history."""
    data = service.get_fastest_speeds(limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.FASTEST_SPEEDS_RETRIEVED)

@router.get("/all-time-winners", response_model=BaseResponse[List[AllTimeWinnerItem]])
def get_all_time_winners(limit: int = Query(15), service: IAnalyticsService = Depends(get_service)):
    """4.8 All-time Grand Prix race winners hall of fame."""
    data = service.get_all_time_winners(limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.ALL_TIME_WINNERS_RETRIEVED)

@router.get("/teammate-qualifying", response_model=BaseResponse[List[TeammateQualiBattleItem]])
def get_teammate_qualifying(year: int = Query(2023), service: IAnalyticsService = Depends(get_service)):
    """4.9 Teammate head-to-head qualifying battle."""
    data = service.get_teammate_qualifying(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.TEAMMATE_QUALIFYING_RETRIEVED)

@router.get("/driver-form", response_model=BaseResponse[List[DriverRollingFormItem]])
def get_driver_form(year: int = Query(2023), service: IAnalyticsService = Depends(get_service)):
    """4.11 Driver rolling form (last 5 races moving average)."""
    data = service.get_driver_form(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.DRIVER_FORM_RETRIEVED)

@router.get("/points-progression", response_model=BaseResponse[List[CumulativePointsItem]])
def get_points_progression(year: int = Query(2023), service: IAnalyticsService = Depends(get_service)):
    """4.12 Cumulative season points progression trajectory."""
    data = service.get_points_progression(year)
    return BaseResponse.ok(data=data, message=SuccessMessage.POINTS_PROGRESSION_RETRIEVED)

@router.get("/constructor-one-twos", response_model=BaseResponse[List[ConstructorOneTwoItem]])
def get_constructor_one_twos(service: IAnalyticsService = Depends(get_service)):
    """4.13 Constructor 1-2 finishes team dominance analysis."""
    data = service.get_constructor_one_twos()
    return BaseResponse.ok(data=data, message=SuccessMessage.CONSTRUCTOR_ONE_TWOS_RETRIEVED)

@router.get("/youngest-winners", response_model=BaseResponse[List[YoungestWinnerItem]])
def get_youngest_winners(limit: int = Query(10), service: IAnalyticsService = Depends(get_service)):
    """4.14 Youngest race winners in F1 history."""
    data = service.get_youngest_winners(limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.YOUNGEST_WINNERS_RETRIEVED)

@router.get("/circuit-masters", response_model=BaseResponse[List[CircuitMasterItem]])
def get_circuit_masters(limit: int = Query(15), service: IAnalyticsService = Depends(get_service)):
    """4.15 Drivers with most wins at specific circuits."""
    data = service.get_circuit_masters(limit)
    return BaseResponse.ok(data=data, message=SuccessMessage.CIRCUIT_MASTERS_RETRIEVED)

@router.get("/last-sync", response_model=BaseResponse[Optional[LastSyncMetadataItem]])
def get_last_sync(service: IAnalyticsService = Depends(get_service)):
    """Get latest database ETL synchronization timestamp and status."""
    data = service.get_last_sync_metadata()
    message = "Last sync metadata retrieved." if data else "No ETL metadata found."
    return BaseResponse.ok(data=data, message=message)
