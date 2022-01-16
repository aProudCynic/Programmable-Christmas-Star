from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from inspect import signature
import logging

from controller.blinkt.blinkt_controller import BlinktController
from controller.blinkt.light_programmes import (
    perform_walk_through_pixels,
    perform_blink_random_colour,
    perform_radiate_colour,
)
from model.request_parameters import (
    WalkThroughPixelsParameters,
    RadiateColourParameters,
)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

light_controller = BlinktController()

logger = logging.getLogger(__name__)

@app.post("/start/walk_through_pixels")
async def walk_through_pixels(parameters: WalkThroughPixelsParameters):
    light_controller.start_loop_with_ttl(perform_walk_through_pixels, parameters)

@app.post("/start/blink_random_colour")
async def blink_random_colour():
    light_controller.start_loop_with_ttl(perform_blink_random_colour, None)

@app.post("/start/radiate_colour")
async def radiate_colour(parameters: RadiateColourParameters):
    light_controller.start_loop_with_ttl(perform_radiate_colour, parameters)


@app.post("/stop")
def stop_light_programme():
    light_controller.stop_loop()

@app.get("/light_programmes")
def get_light_programmes():
    return __extract_light_programmes()

@app.get("/is_on")
def is_on():
    return light_controller.is_on()

def __extract_light_programmes():
    light_programmes = [
        walk_through_pixels,
        blink_random_colour,
        radiate_colour
    ]
    result = []
    for function in light_programmes:
        parameter_data = []
        function_name = function.__name__
        function_signature = signature(function)
        # TODO generalise, this assumes that the light programmes have only body parameters
        function_parameters = function_signature.parameters.values()
        for param in function_parameters:
            parameter_class_name = param.annotation.__name__
            parameter_class = globals()[parameter_class_name]
            parameter_vars = vars(parameter_class)
            parameter_instance_variables = parameter_vars['__fields__']
            for parameter_instance_variable in parameter_instance_variables:
                # this travesty is required because Pydantic ModelField doesn't even have __dict__
                key_value_pairs = str(parameter_instance_variables[parameter_instance_variable]).split()
                parameter_name = key_value_pairs[0][len("name='"):-1]
                parameter_type = key_value_pairs[1][len("type="):]
                parameter_data.append({'name': parameter_name, 'type': parameter_type})
        result.append({'name': function_name, 'parameters': parameter_data})
    return result
