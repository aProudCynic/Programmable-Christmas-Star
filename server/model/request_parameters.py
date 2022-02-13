from pydantic import BaseModel

from model.colour import Colour

class LightProgrammeWithTimeToLive(BaseModel):
    time_to_live: int

class WalkThroughPixelsParameters(LightProgrammeWithTimeToLive):
    colour: Colour

class RadiateColourParameters(LightProgrammeWithTimeToLive):
    colour: Colour
    granularity: int
