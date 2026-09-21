from pydantic import BaseModel
from typing import Optional, List

class SeasonItem(BaseModel):
    year: int
    season_wiki_url: Optional[str] = None

class SeasonCircuitItem(BaseModel):
    year: int
    round: int
    grand_prix_name: str
    circuitId: int
    circuit_name: str
    location: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    circuit_wiki_url: Optional[str] = None
    race_wiki_url: Optional[str] = None

class SeasonDriverItem(BaseModel):
    year: int
    driverId: int
    driver_code: Optional[str] = None
    permanent_number: Optional[float] = None
    full_name: str
    nationality: Optional[str] = None
    driver_wiki_url: Optional[str] = None

class SeasonConstructorItem(BaseModel):
    year: int
    constructorId: int
    constructor_name: str
    constructor_nationality: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class SeasonLineupItem(BaseModel):
    year: int
    team_name: str
    driver_name: str
    driver_code: Optional[str] = None
    car_number: Optional[float] = None
    constructor_wiki_url: Optional[str] = None
    driver_wiki_url: Optional[str] = None

class SeasonWinnerItem(BaseModel):
    round: int
    grand_prix_name: str
    race_date: Optional[str] = None
    circuit_name: str
    winner_name: str
    winning_team: str
    winning_time: Optional[str] = None
    laps_completed: Optional[int] = None
    race_wiki_url: Optional[str] = None
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class SeasonPoleSitterItem(BaseModel):
    round: int
    grand_prix: str
    pole_sitter: str
    team_name: str
    fastest_q3_lap: Optional[str] = None
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None
