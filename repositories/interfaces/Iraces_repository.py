from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class IRacesRepository(ABC):
    @abstractmethod
    def get_race_calendar(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_practice_schedule(self, year: int, round_no: int) -> Optional[Dict[str, Any]]: ...

    @abstractmethod
    def get_sprint_schedule(self, year: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_race_results(self, year: int, round_no: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_qualifying_results(self, year: int, round_no: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_sprint_results(self, year: int, round_no: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_pit_stops(self, year: int, round_no: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_starting_grid(self, year: int, race_id: int) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_lap_chart(self, year: int, round_no: int) -> List[Dict[str, Any]]: ...
