from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    email: str = Field(min_length=1,  max_length=15)
    password: str = Field(min_length=1,  max_length=15)
