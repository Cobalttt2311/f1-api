from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class IDriversRepository(ABC):
    @abstractmethod
    def get_all_drivers(self) -> List[Dict[str, Any]]: ...

    @abstractmethod
    def get_driver_profile(self, driver_id: int) -> Optional[Dict[str, Any]]: ...
