from pydantic import BaseModel
from typing import Optional

class BiggestMoverItem(BaseModel):
    year: int
    grand_prix: str
    driver_name: str
    team_name: str
    starting_grid: int
    finish_position: int
    positions_gained: int
    driver_wiki_url: Optional[str] = None
    race_wiki_url: Optional[str] = None

class PitStopEfficiencyItem(BaseModel):
    team_name: str
    total_pit_stops: int
    avg_duration_seconds: Optional[float] = None
    fastest_stop_seconds: Optional[float] = None
    constructor_wiki_url: Optional[str] = None

class PoleToWinItem(BaseModel):
    year: int
    total_races: int
    pole_and_won_count: int
    pole_to_win_percentage: float

class HighDNFCircuitItem(BaseModel):
    circuit_name: str
    country: Optional[str] = None
    total_dnf_incidents: int
    circuit_wiki_url: Optional[str] = None

class DeepGridWinItem(BaseModel):
    year: int
    grand_prix: str
    driver_name: str
    team_name: str
    starting_grid_position: int
    driver_wiki_url: Optional[str] = None
    race_wiki_url: Optional[str] = None

class LapsLedItem(BaseModel):
    driver_name: str
    total_laps_led: int
    driver_wiki_url: Optional[str] = None

class FastestSpeedItem(BaseModel):
    year: int
    grand_prix: str
    circuit_name: str
    driver_name: str
    max_speed_kmh: Optional[float] = None
    fastestLapTime: Optional[str] = None
    driver_wiki_url: Optional[str] = None
    circuit_wiki_url: Optional[str] = None

class AllTimeWinnerItem(BaseModel):
    driver_name: str
    nationality: Optional[str] = None
    total_race_wins: int
    driver_wiki_url: Optional[str] = None

class TeammateQualiBattleItem(BaseModel):
    team_name: str
    driver_name: str
    outqualified_teammate_count: int
    total_sessions_entered: int

class DriverRollingFormItem(BaseModel):
    year: int
    round: int
    grand_prix: str
    driver_name: str
    points: float
    rolling_avg_points_5_races: Optional[float] = None

class CumulativePointsItem(BaseModel):
    round: int
    grand_prix: str
    driver_name: str
    race_points: float
    cumulative_season_points: float

class ConstructorOneTwoItem(BaseModel):
    team_name: str
    year: int
    total_one_two_finishes: int

class YoungestWinnerItem(BaseModel):
    driver_name: str
    birth_date: Optional[str] = None
    race_date: Optional[str] = None
    grand_prix: str
    year: int
    age_years: Optional[float] = None
    age_months: Optional[float] = None
    age_days: Optional[float] = None
    driver_wiki_url: Optional[str] = None
    race_wiki_url: Optional[str] = None

class CircuitMasterItem(BaseModel):
    circuit_name: str
    country: Optional[str] = None
    driver_name: str
    total_wins_at_circuit: int
    circuit_wiki_url: Optional[str] = None
    driver_wiki_url: Optional[str] = None
