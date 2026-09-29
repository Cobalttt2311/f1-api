from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IStandingsRepository(ABC):
    @abstractmethod
    def get_latest_driver_standings(self) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_latest_constructor_standings(self) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_driver_standings(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_constructor_standings(self, year: int) -> List[Dict[str, Any]]: ...
