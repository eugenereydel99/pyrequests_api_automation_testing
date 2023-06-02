from pydantic import BaseModel


class RegisterRequest(BaseModel):
    email: str
    password: str


class RegisterResponseSuccess(BaseModel):
    id: int
    token: str


class RegisterResponseError(BaseModel):
    error: str
