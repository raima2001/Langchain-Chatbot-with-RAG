from typing import List
from pydantic import BaseModel


class EasyIndexRequest(BaseModel):
    """Request body for index website"""

    website: str


class EasyRAGRequest(BaseModel):
    """Request body for index drive item"""

    query: str
    chat_history: List[str] #Feel free to modify this type as needed
