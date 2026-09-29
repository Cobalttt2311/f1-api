from repositories.interfaces.Iconstructors_repository import IConstructorsRepository
from repositories.constructors_repository import ConstructorsRepository
from services.interfaces.Iconstructors_service import IConstructorsService
from models.constructors import ConstructorItem
from typing import List, Optional

class ConstructorsService(IConstructorsService):
    def __init__(self, repo: Optional[IConstructorsRepository] = None):
        self.repo = repo or ConstructorsRepository()

    def get_all_constructors(self) -> List[ConstructorItem]:
        rows = self.repo.get_all_constructors()
        return [ConstructorItem(**r) for r in rows]
