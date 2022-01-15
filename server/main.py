from fastapi import (
    FastAPI,
    Request,
)
from fastapi.middleware.cors import CORSMiddleware

from json.decoder import JSONDecodeError
import logging

from controller.blinkt.blinkt_controller import BlinktController

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

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@app.post("/start/walk_through_pixels")
async def start_walk_through_pixels(colour: Colour):
    light_controller.start_loop(walk_through_pixels, colour)


@app.post("/stop")
def stop_light_programme():
    light_controller.stop_loop()


@app.get("/light_programmes")
def get_light_programmes():
    return light_controller.get_light_programmes()
