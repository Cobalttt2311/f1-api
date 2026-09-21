from repositories.constructors_repository import ConstructorsRepository
from models.constructors import ConstructorItem
from utils.messages.success_message import SuccessMessage
from utils.responses.base_response import BaseResponse
from typing import List

class ConstructorsService:
    def __init__(self):
        self.repo = ConstructorsRepository()

    def get_all_constructors(self) -> BaseResponse[List[ConstructorItem]]:
        rows = self.repo.get_all_constructors()
        data = [ConstructorItem(**r) for r in rows]
        return BaseResponse.ok(data=data, message=SuccessMessage.CONSTRUCTORS_RETRIEVED)
