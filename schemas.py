from pydantic import BaseModel, EmailStr
from typing import List

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class FileOut(BaseModel):
    id: int
    filename: str

    class Config:
        orm_mode = True