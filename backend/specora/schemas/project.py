from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    prompt: str


class ProjectResponse(BaseModel):
    id: str
    name: str
    prompt: str