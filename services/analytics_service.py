from repositories.interfaces.Ianalytics_repository import IAnalyticsRepository
from repositories.analytics_repository import AnalyticsRepository
from services.interfaces.Ianalytics_service import IAnalyticsService
from datetime import datetime, timezone, timedelta
from models.analytics import (
    LastSyncMetadataItem,
    BiggestMoverItem, PitStopEfficiencyItem, PoleToWinItem,
    HighDNFCircuitItem, DeepGridWinItem, LapsLedItem,
    FastestSpeedItem, AllTimeWinnerItem, TeammateQualiBattleItem,
    DriverRollingFormItem, CumulativePointsItem, ConstructorOneTwoItem,
    YoungestWinnerItem, CircuitMasterItem
)
from typing import List, Optional

class AnalyticsService(IAnalyticsService):
    def __init__(self, repo: Optional[IAnalyticsRepository] = None):
        self.repo = repo or AnalyticsRepository()

    def get_biggest_movers(self, year: int, limit: int = 10) -> List[BiggestMoverItem]:
        rows = self.repo.get_biggest_movers(year, limit)
        return [BiggestMoverItem(**r) for r in rows]

    def get_pit_stop_efficiency(self, year: int) -> List[PitStopEfficiencyItem]:
        rows = self.repo.get_pit_stop_efficiency(year)
        return [PitStopEfficiencyItem(**r) for r in rows]

    def get_pole_to_win_rate(self, start_year: int = 2015) -> List[PoleToWinItem]:
        rows = self.repo.get_pole_to_win_rate(start_year)
        return [PoleToWinItem(**r) for r in rows]

    def get_high_dnf_circuits(self, limit: int = 10) -> List[HighDNFCircuitItem]:
        rows = self.repo.get_high_dnf_circuits(limit)
        return [HighDNFCircuitItem(**r) for r in rows]

    def get_deep_grid_wins(self, min_grid: int = 10, limit: int = 10) -> List[DeepGridWinItem]:
        rows = self.repo.get_deep_grid_wins(min_grid, limit)
        return [DeepGridWinItem(**r) for r in rows]

    def get_most_laps_led(self, limit: int = 15) -> List[LapsLedItem]:
        rows = self.repo.get_most_laps_led(limit)
        return [LapsLedItem(**r) for r in rows]

    def get_fastest_speeds(self, limit: int = 10) -> List[FastestSpeedItem]:
        rows = self.repo.get_fastest_speeds(limit)
        return [FastestSpeedItem(**r) for r in rows]

    def get_all_time_winners(self, limit: int = 15) -> List[AllTimeWinnerItem]:
        rows = self.repo.get_all_time_winners(limit)
        return [AllTimeWinnerItem(**r) for r in rows]

    def get_teammate_qualifying(self, year: int) -> List[TeammateQualiBattleItem]:
        rows = self.repo.get_teammate_qualifying(year)
        return [TeammateQualiBattleItem(**r) for r in rows]

    def get_driver_form(self, year: int) -> List[DriverRollingFormItem]:
        rows = self.repo.get_driver_form(year)
        return [DriverRollingFormItem(**r) for r in rows]

    def get_points_progression(self, year: int) -> List[CumulativePointsItem]:
        rows = self.repo.get_points_progression(year)
        return [CumulativePointsItem(**r) for r in rows]

    def get_constructor_one_twos(self) -> List[ConstructorOneTwoItem]:
        rows = self.repo.get_constructor_one_twos()
        return [ConstructorOneTwoItem(**r) for r in rows]

    def get_youngest_winners(self, limit: int = 10) -> List[YoungestWinnerItem]:
        rows = self.repo.get_youngest_winners(limit)
        return [YoungestWinnerItem(**r) for r in rows]

    def get_circuit_masters(self, limit: int = 15) -> List[CircuitMasterItem]:
        rows = self.repo.get_circuit_masters(limit)
        return [CircuitMasterItem(**r) for r in rows]

    def get_last_sync_metadata(self) -> Optional[LastSyncMetadataItem]:
        row = self.repo.get_last_sync_metadata()
        if not row:
            return None
        
        last_dt = row.get("last_synced_at")
        utc_str = None
        wib_str = None
        if last_dt:
            if isinstance(last_dt, datetime):
                if last_dt.tzinfo is None:
                    last_dt = last_dt.replace(tzinfo=timezone.utc)
                utc_str = last_dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
                wib_dt = last_dt.astimezone(timezone(timedelta(hours=7)))
                wib_str = wib_dt.strftime("%Y-%m-%d %H:%M:%S WIB")
            else:
                utc_str = str(last_dt)
                wib_str = str(last_dt)

        return LastSyncMetadataItem(
            id=row.get("id"),
            last_synced_at_utc=utc_str,
            last_synced_at_wib=wib_str,
            status=row.get("status"),
            total_tables_synced=row.get("total_tables_synced")
        )
