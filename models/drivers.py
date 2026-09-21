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
