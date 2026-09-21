from pydantic import BaseModel
from typing import Optional, List

class RaceCalendarItem(BaseModel):
    raceId: int
    round: int
    grand_prix_name: str
    circuitId: int
    circuit_name: str
    location: Optional[str] = None
    country: Optional[str] = None
    has_sprint: bool = False
    race_date: Optional[str] = None
    race_time_utc: Optional[str] = None
    race_time_wib: Optional[str] = None
    race_datetime_wib: Optional[str] = None
    fp1_date: Optional[str] = None
    fp1_time_utc: Optional[str] = None
    fp1_time_wib: Optional[str] = None
    fp2_date: Optional[str] = None
    fp2_time_utc: Optional[str] = None
    fp2_time_wib: Optional[str] = None
    fp3_date: Optional[str] = None
    fp3_time_utc: Optional[str] = None
    fp3_time_wib: Optional[str] = None
    quali_date: Optional[str] = None
    quali_time_utc: Optional[str] = None
    quali_time_wib: Optional[str] = None
    sprint_date: Optional[str] = None
    sprint_time_utc: Optional[str] = None
    sprint_time_wib: Optional[str] = None
    race_wiki_url: Optional[str] = None
    circuit_wiki_url: Optional[str] = None

class PracticeScheduleItem(BaseModel):
    raceId: int
    year: int
    round: int
    grand_prix_name: str
    circuit_name: str
    country: Optional[str] = None
    fp1_date: Optional[str] = None
    fp1_time_utc: Optional[str] = None
    fp1_time_wib: Optional[str] = None
    fp2_date: Optional[str] = None
    fp2_time_utc: Optional[str] = None
    fp2_time_wib: Optional[str] = None
    fp3_date: Optional[str] = None
    fp3_time_utc: Optional[str] = None
    fp3_time_wib: Optional[str] = None
    race_wiki_url: Optional[str] = None

class SprintScheduleItem(BaseModel):
    raceId: int
    year: int
    round: int
    grand_prix_name: str
    circuit_name: str
    country: Optional[str] = None
    sprint_date: str
    sprint_time_utc: Optional[str] = None
    sprint_time_wib: Optional[str] = None
    sprint_datetime_wib: Optional[str] = None
    main_race_date: Optional[str] = None
    main_race_time_utc: Optional[str] = None
    main_race_time_wib: Optional[str] = None
    race_wiki_url: Optional[str] = None

class RaceResultItem(BaseModel):
    finish_position: str
    car_number: Optional[float] = None
    driver_code: Optional[str] = None
    driver_name: str
    team_name: str
    starting_grid: int
    laps_completed: int
    race_time_or_gap: Optional[str] = None
    points_awarded: float
    status: str
    fastest_lap_time: Optional[str] = None
    fastest_lap_rank: Optional[float] = None
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class QualifyingResultItem(BaseModel):
    qualifying_position: int
    car_number: Optional[float] = None
    driver_code: Optional[str] = None
    driver_name: str
    team_name: str
    q1_time: Optional[str] = None
    q2_time: Optional[str] = None
    q3_time: Optional[str] = None
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class SprintResultItem(BaseModel):
    finish_position: str
    car_number: Optional[float] = None
    driver_code: Optional[str] = None
    driver_name: str
    team_name: str
    starting_grid: int
    laps_completed: int
    time_or_gap: Optional[str] = None
    points_awarded: float
    status: str
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class PitStopItem(BaseModel):
    stop_number: int
    lap: int
    time_of_day_utc: Optional[str] = None
    driver_code: Optional[str] = None
    driver_name: str
    team_name: str
    stop_duration_seconds: Optional[str] = None
    total_stop_milliseconds: Optional[int] = None
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class StartingGridDriver(BaseModel):
    starting_grid_position: str
    car_number: Optional[float] = None
    driver_code: Optional[str] = None
    driver_name: str
    team_name: str
    qualifying_position: Optional[int] = None
    qualifying_best_lap: Optional[str] = None
    grid_status: str
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None
    race_wiki_url: Optional[str] = None

class LapChartItem(BaseModel):
    lap: int
    track_position: int
    driver_code: Optional[str] = None
    driver_name: str
    lap_time_str: Optional[str] = None
    lap_time_ms: Optional[int] = None
