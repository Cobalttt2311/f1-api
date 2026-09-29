from abc import ABC, abstractmethod
from typing import List
from models.seasons import (
    SeasonItem, SeasonCircuitItem, SeasonDriverItem, 
    SeasonConstructorItem, SeasonLineupItem, SeasonWinnerItem, SeasonPoleSitterItem
)

class ISeasonsService(ABC):
    @abstractmethod
    def get_all_seasons(self) -> List[SeasonItem]: ...

    @abstractmethod
    def get_season_circuits(self, year: int) -> List[SeasonCircuitItem]: ...

    @abstractmethod
    def get_season_drivers(self, year: int) -> List[SeasonDriverItem]: ...

    @abstractmethod
    def get_season_constructors(self, year: int) -> List[SeasonConstructorItem]: ...

    @abstractmethod
    def get_season_lineups(self, year: int) -> List[SeasonLineupItem]: ...

    @abstractmethod
    def get_season_winners(self, year: int) -> List[SeasonWinnerItem]: ...

    @abstractmethod
    def get_season_pole_sitters(self, year: int) -> List[SeasonPoleSitterItem]: ...
