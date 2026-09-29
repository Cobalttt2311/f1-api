from abc import ABC, abstractmethod
from typing import List
from models.drivers import DriverItem, DriverProfile

class IDriversService(ABC):
    @abstractmethod
    def get_all_drivers(self) -> List[DriverItem]: ...

    @abstractmethod
    def get_driver_profile(self, driver_id: int) -> DriverProfile: ...
