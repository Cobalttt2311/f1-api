from pydantic import BaseModel
from typing import Optional

class DriverStandingItem(BaseModel):
    season: Optional[int] = None
    after_round: Optional[int] = None
    after_grand_prix: Optional[str] = None
    championship_rank: float
    driver_code: Optional[str] = None
    driver_name: str
    nationality: Optional[str] = None
    team_name: str
    total_points: float
    total_wins: int
    driver_wiki_url: Optional[str] = None
    constructor_wiki_url: Optional[str] = None

class ConstructorStandingItem(BaseModel):
    season: Optional[int] = None
    after_round: Optional[int] = None
    after_grand_prix: Optional[str] = None
    championship_rank: float
    constructor_name: str
    nationality: Optional[str] = None
    total_points: float
    total_wins: int
    constructor_wiki_url: Optional[str] = None
