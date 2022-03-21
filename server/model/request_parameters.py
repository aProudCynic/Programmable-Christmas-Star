from pydantic import BaseModel

from model.colour import Colour

class LightProgrammeWithTimeToLive(BaseModel):
    time_to_live: int

class BlinkRandomColoursParameters(LightProgrammeWithTimeToLive):
    pass

class WalkThroughPixelsParameters(LightProgrammeWithTimeToLive):
    colour: Colour

class RadiateColourParameters(LightProgrammeWithTimeToLive):
    colour: Colour
    granularity: int

class DifferentColourParameters(LightProgrammeWithTimeToLive):
    colour_1: Colour
    colour_2: Colour
    colour_3: Colour
    colour_4: Colour
    colour_5: Colour
    colour_6: Colour
    colour_7: Colour
    colour_8: Colour
