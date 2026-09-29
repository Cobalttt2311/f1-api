from abc import ABC, abstractmethod
from typing import List
from models.standings import DriverStandingItem, ConstructorStandingItem

class IStandingsService(ABC):
    @abstractmethod
    def get_latest_driver_standings(self) -> List[DriverStandingItem]: ...

    @abstractmethod
    def get_latest_constructor_standings(self) -> List[ConstructorStandingItem]: ...

    @abstractmethod
    def get_season_driver_standings(self, year: int) -> List[DriverStandingItem]: ...

    @abstractmethod
    def get_season_constructor_standings(self, year: int) -> List[ConstructorStandingItem]: ...
