from pydantic import BaseModel

from model.colour import Colour

class WalkThroughPixelsParameters(BaseModel):
    colour: Colour
