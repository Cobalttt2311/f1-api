from abc import ABC, abstractmethod
from typing import List
from models.races import (
    RaceCalendarItem, PracticeScheduleItem, SprintScheduleItem,
    RaceResultItem, QualifyingResultItem, SprintResultItem,
    PitStopItem, StartingGridDriver, LapChartItem
)

class IRacesService(ABC):
    @abstractmethod
    def get_race_calendar(self, year: int) -> List[RaceCalendarItem]: ...

    @abstractmethod
    def get_practice_schedule(self, year: int, round_no: int) -> PracticeScheduleItem: ...

    @abstractmethod
    def get_sprint_schedule(self, year: int) -> List[SprintScheduleItem]: ...

    @abstractmethod
    def get_race_results(self, year: int, round_no: int) -> List[RaceResultItem]: ...

    @abstractmethod
    def get_qualifying_results(self, year: int, round_no: int) -> List[QualifyingResultItem]: ...

    @abstractmethod
    def get_sprint_results(self, year: int, round_no: int) -> List[SprintResultItem]: ...

    @abstractmethod
    def get_pit_stops(self, year: int, round_no: int) -> List[PitStopItem]: ...

    @abstractmethod
    def get_starting_grid(self, year: int, race_id: int) -> List[StartingGridDriver]: ...

    @abstractmethod
    def get_lap_chart(self, year: int, round_no: int) -> List[LapChartItem]: ...
