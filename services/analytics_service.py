from repositories.analytics_repository import AnalyticsRepository
from models.analytics import (
    BiggestMoverItem, PitStopEfficiencyItem, PoleToWinItem,
    HighDNFCircuitItem, DeepGridWinItem, LapsLedItem,
    FastestSpeedItem, AllTimeWinnerItem, TeammateQualiBattleItem,
    DriverRollingFormItem, CumulativePointsItem, ConstructorOneTwoItem,
    YoungestWinnerItem, CircuitMasterItem
)
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List

class AnalyticsService:
    def __init__(self):
        self.repo = AnalyticsRepository()

    def get_biggest_movers(self, year: int, limit: int = 10) -> BaseResponse[List[BiggestMoverItem]]:
        rows = self.repo.get_biggest_movers(year, limit)
        data = [BiggestMoverItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.BIGGEST_MOVERS_RETRIEVED)

    def get_pit_stop_efficiency(self, year: int) -> BaseResponse[List[PitStopEfficiencyItem]]:
        rows = self.repo.get_pit_stop_efficiency(year)
        data = [PitStopEfficiencyItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.PIT_STOP_EFFICIENCY_RETRIEVED)

    def get_pole_to_win_rate(self, start_year: int = 2015) -> BaseResponse[List[PoleToWinItem]]:
        rows = self.repo.get_pole_to_win_rate(start_year)
        data = [PoleToWinItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.POLE_TO_WIN_RETRIEVED)

    def get_high_dnf_circuits(self, limit: int = 10) -> BaseResponse[List[HighDNFCircuitItem]]:
        rows = self.repo.get_high_dnf_circuits(limit)
        data = [HighDNFCircuitItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.HIGH_DNF_CIRCUITS_RETRIEVED)

    def get_deep_grid_wins(self, min_grid: int = 10, limit: int = 10) -> BaseResponse[List[DeepGridWinItem]]:
        rows = self.repo.get_deep_grid_wins(min_grid, limit)
        data = [DeepGridWinItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.DEEP_GRID_WINS_RETRIEVED)

    def get_most_laps_led(self, limit: int = 15) -> BaseResponse[List[LapsLedItem]]:
        rows = self.repo.get_most_laps_led(limit)
        data = [LapsLedItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.MOST_LAPS_LED_RETRIEVED)

    def get_fastest_speeds(self, limit: int = 10) -> BaseResponse[List[FastestSpeedItem]]:
        rows = self.repo.get_fastest_speeds(limit)
        data = [FastestSpeedItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.FASTEST_SPEEDS_RETRIEVED)

    def get_all_time_winners(self, limit: int = 15) -> BaseResponse[List[AllTimeWinnerItem]]:
        rows = self.repo.get_all_time_winners(limit)
        data = [AllTimeWinnerItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.ALL_TIME_WINNERS_RETRIEVED)

    def get_teammate_qualifying(self, year: int) -> BaseResponse[List[TeammateQualiBattleItem]]:
        rows = self.repo.get_teammate_qualifying(year)
        data = [TeammateQualiBattleItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.TEAMMATE_QUALIFYING_RETRIEVED)

    def get_driver_form(self, year: int) -> BaseResponse[List[DriverRollingFormItem]]:
        rows = self.repo.get_driver_form(year)
        data = [DriverRollingFormItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.DRIVER_FORM_RETRIEVED)

    def get_points_progression(self, year: int) -> BaseResponse[List[CumulativePointsItem]]:
        rows = self.repo.get_points_progression(year)
        data = [CumulativePointsItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.POINTS_PROGRESSION_RETRIEVED)

    def get_constructor_one_twos(self) -> BaseResponse[List[ConstructorOneTwoItem]]:
        rows = self.repo.get_constructor_one_twos()
        data = [ConstructorOneTwoItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.CONSTRUCTOR_ONE_TWOS_RETRIEVED)

    def get_youngest_winners(self, limit: int = 10) -> BaseResponse[List[YoungestWinnerItem]]:
        rows = self.repo.get_youngest_winners(limit)
        data = [YoungestWinnerItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.YOUNGEST_WINNERS_RETRIEVED)

    def get_circuit_masters(self, limit: int = 15) -> BaseResponse[List[CircuitMasterItem]]:
        rows = self.repo.get_circuit_masters(limit)
        data = [CircuitMasterItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.CIRCUIT_MASTERS_RETRIEVED)
