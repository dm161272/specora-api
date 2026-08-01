from pydantic import BaseModel
from typing import List


class FieldSpec(BaseModel):
    name: str
    type: str


class EntitySpec(BaseModel):
    name: str
    fields: List[FieldSpec]


class EndpointSpec(BaseModel):
    method: str
    path: str
    description: str


class ApiSpecification(BaseModel):
    name: str
    description: str
    database: str
    authentication: str
    entities: List[EntitySpec]
    endpoints: List[EndpointSpec]