from abc import ABC, abstractmethod
from typing import List, Optional
from models.analytics import (
    LastSyncMetadataItem,
    BiggestMoverItem, PitStopEfficiencyItem, PoleToWinItem,
    HighDNFCircuitItem, DeepGridWinItem, LapsLedItem,
    FastestSpeedItem, AllTimeWinnerItem, TeammateQualiBattleItem,
    DriverRollingFormItem, CumulativePointsItem, ConstructorOneTwoItem,
    YoungestWinnerItem, CircuitMasterItem
)

class IAnalyticsService(ABC):
    @abstractmethod
    def get_biggest_movers(self, year: int, limit: int = 10) -> List[BiggestMoverItem]: ...

    @abstractmethod
    def get_pit_stop_efficiency(self, year: int) -> List[PitStopEfficiencyItem]: ...

    @abstractmethod
    def get_pole_to_win_rate(self, start_year: int = 2015) -> List[PoleToWinItem]: ...

    @abstractmethod
    def get_high_dnf_circuits(self, limit: int = 10) -> List[HighDNFCircuitItem]: ...

    @abstractmethod
    def get_deep_grid_wins(self, min_grid: int = 10, limit: int = 10) -> List[DeepGridWinItem]: ...

    @abstractmethod
    def get_most_laps_led(self, limit: int = 15) -> List[LapsLedItem]: ...

    @abstractmethod
    def get_fastest_speeds(self, limit: int = 10) -> List[FastestSpeedItem]: ...

    @abstractmethod
    def get_all_time_winners(self, limit: int = 15) -> List[AllTimeWinnerItem]: ...

    @abstractmethod
    def get_teammate_qualifying(self, year: int) -> List[TeammateQualiBattleItem]: ...

    @abstractmethod
    def get_driver_form(self, year: int) -> List[DriverRollingFormItem]: ...

    @abstractmethod
    def get_points_progression(self, year: int) -> List[CumulativePointsItem]: ...

    @abstractmethod
    def get_constructor_one_twos(self) -> List[ConstructorOneTwoItem]: ...

    @abstractmethod
    def get_youngest_winners(self, limit: int = 10) -> List[YoungestWinnerItem]: ...

    @abstractmethod
    def get_circuit_masters(self, limit: int = 15) -> List[CircuitMasterItem]: ...

    @abstractmethod
    def get_last_sync_metadata(self) -> Optional[LastSyncMetadataItem]: ...
