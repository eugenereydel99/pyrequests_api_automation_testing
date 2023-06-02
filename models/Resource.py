from pydantic import BaseModel


class Resource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str
