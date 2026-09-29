from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ISeasonsRepository(ABC):
    @abstractmethod
    def get_all_seasons(self) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_circuits(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_drivers(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_constructors(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_lineups(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_winners(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_season_pole_sitters(self, year: int) -> List[Dict[str, Any]]: ...
