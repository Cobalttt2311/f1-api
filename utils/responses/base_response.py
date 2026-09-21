"""
Generic Base Response Model for Standardized JSON Responses
"""

from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Operation completed successfully."
    data: Optional[T] = None

    @classmethod
    def ok(cls, data: T, message: str = "Data retrieved successfully.") -> "BaseResponse[T]":
        return cls(success=True, message=message, data=data)

    @classmethod
    def error(cls, message: str, data: Optional[Any] = None) -> "BaseResponse[Any]":
        return cls(success=False, message=message, data=data)
