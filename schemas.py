from pydantic import BaseModel
from typing import List

class ResearchRequest(BaseModel):
    trade: str
    city: str
    state: str
    min_bond: int
    keywords: List[str]