from pydantic import BaseModel
from typing import Optional

class ConstructorItem(BaseModel):
    constructorId: int
    constructorRef: str
    constructor_name: str
    constructor_nationality: Optional[str] = None
    constructor_wiki_url: Optional[str] = None
