from pydantic import BaseModel
from typing import Optional

class DriverItem(BaseModel):
    driverId: int
    driverRef: str
    driver_code: Optional[str] = None
    permanent_number: Optional[float] = None
    full_name: str
    nationality: Optional[str] = None
    date_of_birth: Optional[str] = None
    driver_wiki_url: Optional[str] = None

class DriverProfile(BaseModel):
    driverId: int
    full_name: str
    driver_code: Optional[str] = None
    permanent_number: Optional[float] = None
    birth_date: Optional[str] = None
    nationality: Optional[str] = None
    driver_wiki_url: Optional[str] = None
    total_races_entered: int
    total_career_wins: int
    total_career_podiums: int
    total_career_points: float
    total_career_poles: int = 0
    total_fastest_laps: int = 0
    total_dnfs: int = 0
    world_championships: int = 0
    highest_grid: Optional[int] = None
    seasons_active: Optional[str] = None
    teams_driven_for: Optional[str] = None
    season_year: Optional[int] = None
    season_position: Optional[int] = None
    season_points: Optional[float] = None
    season_team: Optional[str] = None
