from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from inspect import signature
import logging

from controller.blinkt.blinkt_controller import BlinktController
from model.colour import Colour
from controller.blinkt.light_programmes import perform_walk_through_pixels

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
async def walk_through_pixels(colour: Colour):
    light_controller.start_loop(perform_walk_through_pixels, colour)


@app.post("/stop")
def stop_light_programme():
    light_controller.stop_loop()


@app.get("/light_programmes")
def get_light_programmes():
    return __extract_light_programmes()

def __extract_light_programmes():
    result = []
    for function in (
        walk_through_pixels,
    ):
        function_name = function.__name__
        function_signature = signature(function)
        function_parameters = function_signature.parameters.values()
        function_parameter_data = [{'name': param.name, 'type': param.annotation.__name__} for param in function_parameters]
        result.append({'name': function_name, 'parameters': function_parameter_data})
    print(result)
    return result
