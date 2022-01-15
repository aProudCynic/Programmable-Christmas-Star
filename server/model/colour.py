from pydantic import BaseModel

class Colour(BaseModel):

    red: int
    green: int
    blue: int
