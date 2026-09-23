from fastapi import APIRouter, Depends, Query
from services.analytics_service import AnalyticsService
from models.analytics import (
    BiggestMoverItem, PitStopEfficiencyItem, PoleToWinItem,
    HighDNFCircuitItem, DeepGridWinItem, LapsLedItem,
    FastestSpeedItem, AllTimeWinnerItem, TeammateQualiBattleItem,
    DriverRollingFormItem, CumulativePointsItem, ConstructorOneTwoItem,
    YoungestWinnerItem, CircuitMasterItem,
    LastSyncMetadataItem
)
from utils.responses.base_response import BaseResponse
from typing import List, Optional

router = APIRouter(prefix="/analytics", tags=["Strategy & Performance Analytics"])

def get_service() -> AnalyticsService:
    return AnalyticsService()

@router.get("/biggest-movers", response_model=BaseResponse[List[BiggestMoverItem]])
def get_biggest_movers(year: int = Query(2023), limit: int = Query(10), service: AnalyticsService = Depends(get_service)):
    """4.1 Greatest comebacks / positions gained from starting grid."""
    return service.get_biggest_movers(year, limit)

@router.get("/pit-stop-efficiency", response_model=BaseResponse[List[PitStopEfficiencyItem]])
def get_pit_stop_efficiency(year: int = Query(2023), service: AnalyticsService = Depends(get_service)):
    """4.2 Pit stop efficiency and average duration by constructor."""
    return service.get_pit_stop_efficiency(year)

@router.get("/pole-to-win-rate", response_model=BaseResponse[List[PoleToWinItem]])
def get_pole_to_win_rate(start_year: int = Query(2015), service: AnalyticsService = Depends(get_service)):
    """4.3 Pole-to-win conversion rate across seasons."""
    return service.get_pole_to_win_rate(start_year)

@router.get("/high-dnf-circuits", response_model=BaseResponse[List[HighDNFCircuitItem]])
def get_high_dnf_circuits(limit: int = Query(10), service: AnalyticsService = Depends(get_service)):
    """4.4 Most incident-prone and high-DNF circuits."""
    return service.get_high_dnf_circuits(limit)

@router.get("/deep-grid-wins", response_model=BaseResponse[List[DeepGridWinItem]])
def get_deep_grid_wins(min_grid: int = Query(10), limit: int = Query(10), service: AnalyticsService = Depends(get_service)):
    """4.5 Historical wins from deepest starting grid positions (P10+)."""
    return service.get_deep_grid_wins(min_grid, limit)

@router.get("/most-laps-led", response_model=BaseResponse[List[LapsLedItem]])
def get_most_laps_led(limit: int = Query(15), service: AnalyticsService = Depends(get_service)):
    """4.6 Drivers with most laps led in P1 across history."""
    return service.get_most_laps_led(limit)

@router.get("/fastest-speeds", response_model=BaseResponse[List[FastestSpeedItem]])
def get_fastest_speeds(limit: int = Query(10), service: AnalyticsService = Depends(get_service)):
    """4.7 Fastest race speed recorded in history."""
    return service.get_fastest_speeds(limit)

@router.get("/all-time-winners", response_model=BaseResponse[List[AllTimeWinnerItem]])
def get_all_time_winners(limit: int = Query(15), service: AnalyticsService = Depends(get_service)):
    """4.8 All-time Grand Prix race winners hall of fame."""
    return service.get_all_time_winners(limit)

@router.get("/teammate-qualifying", response_model=BaseResponse[List[TeammateQualiBattleItem]])
def get_teammate_qualifying(year: int = Query(2023), service: AnalyticsService = Depends(get_service)):
    """4.9 Teammate head-to-head qualifying battle."""
    return service.get_teammate_qualifying(year)

@router.get("/driver-form", response_model=BaseResponse[List[DriverRollingFormItem]])
def get_driver_form(year: int = Query(2023), service: AnalyticsService = Depends(get_service)):
    """4.11 Driver rolling form (last 5 races moving average)."""
    return service.get_driver_form(year)

@router.get("/points-progression", response_model=BaseResponse[List[CumulativePointsItem]])
def get_points_progression(year: int = Query(2023), service: AnalyticsService = Depends(get_service)):
    """4.12 Cumulative season points progression trajectory."""
    return service.get_points_progression(year)

@router.get("/constructor-one-twos", response_model=BaseResponse[List[ConstructorOneTwoItem]])
def get_constructor_one_twos(service: AnalyticsService = Depends(get_service)):
    """4.13 Constructor 1-2 finishes team dominance analysis."""
    return service.get_constructor_one_twos()

@router.get("/youngest-winners", response_model=BaseResponse[List[YoungestWinnerItem]])
def get_youngest_winners(limit: int = Query(10), service: AnalyticsService = Depends(get_service)):
    """4.14 Youngest race winners in F1 history."""
    return service.get_youngest_winners(limit)

@router.get("/circuit-masters", response_model=BaseResponse[List[CircuitMasterItem]])
def get_circuit_masters(limit: int = Query(15), service: AnalyticsService = Depends(get_service)):
    """4.15 Drivers with most wins at specific circuits."""
    return service.get_circuit_masters(limit)

@router.get("/last-sync", response_model=BaseResponse[Optional[LastSyncMetadataItem]])
def get_last_sync(service: AnalyticsService = Depends(get_service)):
    """Get latest database ETL synchronization timestamp and status."""
    return service.get_last_sync_metadata()
