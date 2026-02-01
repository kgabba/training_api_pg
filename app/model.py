from pydantic import BaseModel, Field, EmailStr

class Otzyv(BaseModel):
    text: str = Field(max_length=500, min_length=2)
    mail: EmailStr
    phone: int = Field(ge=70000000000, le=79999999999)
    mood: str|None = None