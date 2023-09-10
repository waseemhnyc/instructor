# generated by datamodel-codegen:
#   filename:  input.json
#   timestamp: 2023-09-10T00:33:42+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel


class Type(Enum):
    home = 'home'
    work = 'work'
    mobile = 'mobile'


class PhoneNumber(BaseModel):
    type: Type
    number: str


class ExtractPerson(BaseModel):
    name: str
    age: int
    phoneNumbers: List[PhoneNumber]
