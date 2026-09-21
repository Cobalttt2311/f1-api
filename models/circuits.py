from pydantic import BaseModel
from typing import Optional, List

class CircuitItem(BaseModel):
    circuitId: int
    circuitRef: str
    circuit_name: str
    location: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude_meters: Optional[int] = None
    circuit_wiki_url: Optional[str] = None

class CircuitHistoryWinner(BaseModel):
    year: int
    grand_prix_name: str
    winner_name: str
    winning_team: str
    winning_time: Optional[str] = None
    race_wiki_url: Optional[str] = None
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None
